# Author: Scott Woods <scott.18.ansar@gmail.com.com>
# MIT License
#
# Copyright (c) 2022, 2023 Scott Woods
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""".

.
"""
__docformat__ = 'restructuredtext'

__all__ = [
	'NetworkSettings',
	'AccountSettings',
	'AccessSettings',
	'procedure_network',
	'procedure_signup',
	'procedure_login',
	'procedure_account',
	'procedure_access',
]

import os
import getpass
import uuid
import ansar.connect as ar
from ansar.encode.args import QUOTED_TYPE, SHIPMENT_WITH_QUOTES, SHIPMENT_WITHOUT_QUOTES
from ansar.create.procedure import DEFAULT_HOME, DEFAULT_GROUP, HOME, GROUP
from ansar.create.procedure import open_home, role_status
from .foh_if import *
from .wan import *
from .product import *
from .directory_if import *

DEFAULT_ACCOUNT_ACTION = 'show'

# Per-command arguments as required.
# e.g. command-line parameters specific to create.
class NetworkSettings(object):
	def __init__(self, group_name=None, home_path=None, show_scopes=None, connect_scope=None, connect_file=None):
		self.group_name = group_name
		self.home_path = home_path
		self.show_scopes = show_scopes
		self.connect_scope = connect_scope
		self.connect_file = connect_file

NETWORK_SETTINGS_SCHEMA = {
	'group_name': ar.Unicode(),
	'home_path': ar.Unicode(),
	'show_scopes': ar.Boolean(),
	'connect_scope': ScopeOfService,
	'connect_file': ar.Unicode(),
}

ar.bind(NetworkSettings, object_schema=NETWORK_SETTINGS_SCHEMA)

#
#
def procedure_network(self, network, group, home):
	group = ar.word_argument_2(group, network.group_name, DEFAULT_GROUP, GROUP)
	home = ar.word_argument_2(home, network.home_path, DEFAULT_HOME, HOME)

	if '.' in group:
		e = ar.Rejected(group_name=(group, f'no-dots name'))
		raise ar.Incomplete(e)
	group_role = f'group.{group}'

	hb = open_home(home)

	_, running = role_status(self, hb, [group_role])
	if running:
		e = ar.Failed(group_start=(f'group "{group}" is already running', None))
		raise ar.Incomplete(e)

	settings = []
	if network.connect_scope:	# Assignment of new connection.
		if not network.connect_file:
			e = ar.Rejected(connect_with_no_file=('missing connection details', None))
			raise ar.Incomplete(e)
		s = ScopeOfService.to_name(network.connect_scope)
		p = os.path.abspath(network.connect_file)
		settings.append(f'--connect-scope={s}')
		settings.append(f'--connect-file={p}')

	else:
		settings.append(f'--show-scopes')

	try:
		a = self.create(ar.Process, 'ansar-group',	
					origin=ar.POINT_OF_ORIGIN.RUN_ORIGIN,
					home_path=hb.home_path, role_name=group_role, subrole=False,
					settings=settings)

		# Wait for Ack from new process to verify that
		# framework is operational.
		m = self.select(ar.Completed, ar.Stop)
		if isinstance(m, ar.Stop):
			# Honor the slim chance of a control-c before
			# the framework can respond.
			self.send(m, a)
			m = self.select(ar.Completed)

		# Process.
		def lfa_text(lfa):
			f, l, a = len(d.listing), len(d.find), len(d.accepted)
			s = f'{f}/{l}/{a}'
			return s

		value = m.value
		if isinstance(value, ar.Ack):	   # New instance established itself.
			pass
		elif isinstance(value, DirectoryAncestry):
			for d in reversed(value.lineage):
				scope = ScopeOfService.to_name(d.scope) if d.scope else '?'
				ipp = str(d.connecting_ipp) if d.connecting_ipp.host else 'DISABLED'
				method = d.method if d.connecting_ipp.host else '-'
				started = ar.world_to_text(d.started) if d.started else '-'
				connected = ar.world_to_text(d.connected) if d.connected else '-'
				sc = f'{started}'
				lfa = lfa_text(d)
				ar.output_line(f'{scope:6} {ipp:20} {method:26} {sc:26} {lfa}')
				key_name = {k: r.search_or_listing for r in d.listing for k in r.route_key}
				for r in d.listing:
					ar.output_line(f'[P] {r.search_or_listing} ({len(r.route_key)})', tab=1)
				for r in d.find:
					ar.output_line(f'[S] {r.search_or_listing} ({len(r.route_key)})', tab=1)
					for k in r.route_key:
						ar.output_line(f'[R] {key_name[k]}', tab=2)
				for a in d.accepted:
					ar.output_line(f'[A] {a}', tab=1)

		elif isinstance(value, NetworkConnect):
			return value
		elif isinstance(value, ar.Faulted):
			raise ar.Incomplete(value)
		elif isinstance(value, ar.LockedOut):
			e = ar.Failed(role_lock=(None, f'"{group_role}" already running as <{value.pid}>'))
			raise ar.Incomplete(e)
		else:
			e = ar.Failed(role_execute=(value, f'unexpected response from "{group_role}" (ansar-group)'))
			raise ar.Incomplete(e)
	finally:
		pass

	return None

# Keyboard input.
# Form/field filling.
def fill_field(name, t):
	if name == 'password':
		d = getpass.getpass(f'Password: ')
		return d

	ip = name.capitalize()
	ip = ip.replace('_', ' ')
	kb = input(f'{ip}: ')

	if isinstance(t, QUOTED_TYPE):
		sh = SHIPMENT_WITH_QUOTES % (kb,)
	else:
		sh = SHIPMENT_WITHOUT_QUOTES % (kb,)
	try:
		encoding = ar.CodecJson()
		d, _ = encoding.decode(sh, t)
	except ar.CodecFailed as e:
		f = ar.Faulted(f'cannot accept input for "{ip}"', str(e))
		raise ar.Incomplete(f)
	return d

def fill_form(self, form):
	schema = form.__art__.value
	for k, v in schema.items():
		if k == 'login_token':
			continue
		t = getattr(form, k, None)
		if t is not None:
			continue
		d = fill_field(k, v)
		setattr(form, k, d)

#
#
class AccountSettings(object):
	def __init__(self, read=False, update=False, delete=False, organization_name=None, organization_location=None):
		self.read = read
		self.update = update
		self.delete = delete
		self.organization_name = organization_name
		self.organization_location = organization_location

ACCOUNT_SETTINGS_SCHEMA = {
	'read': ar.Boolean(),
	'update': ar.Boolean(),
	'delete': ar.Boolean(),
	'organization_name': ar.Unicode(),
	'organization_location': ar.Unicode(),
}

ar.bind(AccountSettings, object_schema=ACCOUNT_SETTINGS_SCHEMA)

# Standardize checking and diagnostics for all the
# cloud interactions.
def crud_address_and_token(crud, ipp, token):
	if crud > 1:
		f = ar.Faulted('multiple operations specified', 'not supported')
		return f
	if not ipp:
		f = ar.Faulted('no address defined for the ansar cloud', 'use --cloud-ip=<address> --store-settings')
		return f
	if not token:
		f = ar.Faulted('not logged in', 'need to signup or login')
		return f
	return None

# Create a new account.
def procedure_signup(self, account):
	settings = ar.object_custom_settings()
	cloud_ip = settings.cloud_ip

	f = crud_address_and_token(1, cloud_ip, uuid.uuid4())
	if f:
		return f

	ar.connect(self, ar.HostPort(cloud_ip, FOH_PORT))
	m = self.select(ar.Connected, ar.NotConnected, ar.Stop)
	if isinstance(m, ar.Connected):
		session = self.return_address
	elif isinstance(m, ar.NotConnected):
		return m
	else:
		return ar.Aborted()

	try:
		return account_signup(self, session)	# Create account in cloud, clobber token.
	finally:
		self.send(ar.Close(), session)
		self.select(ar.Closed, ar.Stop)

# Refresh the session with an account.
def procedure_login(self, account):
	settings = ar.object_custom_settings()
	cloud_ip = settings.cloud_ip

	f = crud_address_and_token(1, cloud_ip, uuid.uuid4())
	if f:
		return f

	ar.connect(self, ar.HostPort(cloud_ip, FOH_PORT))
	m = self.select(ar.Connected, ar.NotConnected, ar.Stop)
	if isinstance(m, ar.Connected):
		session = self.return_address
	elif isinstance(m, ar.NotConnected):
		return m
	else:
		return ar.Aborted()

	try:
		return account_login(self, session)		# Creds for existing account, update token.
	finally:
		self.send(ar.Close(), session)
		self.select(ar.Closed, ar.Stop)

# CRUD for the account entity. Well, more like RUD as
# the create part is covered by signup and login.
def procedure_account(self, account):
	settings = ar.object_custom_settings()
	cloud_ip = settings.cloud_ip
	login_token = settings.login_token

	crud = sum([account.read, account.update, account.delete])

	f = crud_address_and_token(crud, cloud_ip, login_token)
	if f:
		return f

	ar.connect(self, ar.HostPort(cloud_ip, FOH_PORT))
	m = self.select(ar.Connected, ar.NotConnected, ar.Stop)
	if isinstance(m, ar.Connected):
		session = self.return_address
	elif isinstance(m, ar.NotConnected):
		return m
	else:
		return ar.Aborted()

	try:
		if account.update:
			return account_update(self, login_token, session, account)
		elif account.delete:
			return account_delete(self, login_token, session)
		return account_read(self, login_token, session)
	finally:
		self.send(ar.Close(), session)
		self.select(ar.Closed, ar.Stop)

def account_signup(self, session):
	signup = AccountSignup()
	fill_form(self, signup)
	self.send(signup, session)
	m = self.select(AccountOpened, ar.Faulted, ar.Abandoned, ar.Stop)
	if isinstance(m, AccountOpened):
		pass
	elif isinstance(m, ar.Faulted):
		return m
	elif isinstance(m, ar.Abandoned):
		f = ar.Faulted('remote abandoned connection', 'try later?')
		return f
	else:
		return ar.Aborted()

	settings = ar.object_custom_settings()
	settings.login_token = m.login_token
	ar.store_settings(settings)
	return None

def account_login(self, session):
	login = AccountLogin()
	fill_form(self, login)
	self.send(login, session)
	m = self.select(AccountOpened, ar.Faulted, ar.Abandoned, ar.Stop)
	if isinstance(m, AccountOpened):
		pass
	elif isinstance(m, ar.Faulted):
		return m
	elif isinstance(m, ar.Abandoned):
		f = ar.Faulted('remote abandoned connection', 'try later?')
		return f
	else:
		return ar.Aborted()

	settings = ar.object_custom_settings()
	settings.login_token = m.login_token
	ar.store_settings(settings)
	return None

def account_read(self, login_token, session):
	read = AccountRead(login_token=login_token)
	self.send(read, session)
	m = self.select(AccountPage, ar.Faulted, ar.Abandoned, ar.Stop)
	if isinstance(m, AccountPage):
		return m
	elif isinstance(m, ar.Faulted):
		return m
	elif isinstance(m, ar.Abandoned):
		f = ar.Faulted('remote abandoned connection', 'try later?')
		return f
	else:
		return ar.Aborted()
	return None

def account_update(self, login_token, session, account):
	update = AccountUpdate(login_token=login_token,
		organization_name=account.organization_name, organization_location=account.organization_location)

	if not account.organization_name and not account.organization_location:
		fill_form(self, update)
	self.send(update, session)
	m = self.select(AccountPage, ar.Faulted, ar.Abandoned, ar.Stop)
	if isinstance(m, AccountPage):
		return m
	elif isinstance(m, ar.Faulted):
		return m
	elif isinstance(m, ar.Abandoned):
		f = ar.Faulted('remote abandoned connection', 'try later?')
		return f
	else:
		return ar.Aborted()
	return None

def account_delete(self, login_token, session):
	delete = AccountDelete(login_token=login_token)
	self.send(delete, session)
	m = self.select(AccountDeleted, ar.Faulted, ar.Abandoned, ar.Stop)
	if isinstance(m, AccountDeleted):
		return None
	elif isinstance(m, ar.Faulted):
		return m
	elif isinstance(m, ar.Abandoned):
		f = ar.Faulted('remote abandoned connection', 'try later?')
		return f
	else:
		return ar.Aborted()
	return None

#
#
class AccessSettings(object):
	def __init__(self, read=False, update=False, export=False, export_file=None,
			product_name=None, product_instance=None, access_scope=None,
			custom_host=None, custom_port=None,
			fixed_access=None,
			access_id=None, access_name=None):
		self.read = read
		self.update = update
		self.export = export
		self.export_file = export_file
		self.product_name = product_name
		self.product_instance = product_instance
		self.access_scope = access_scope
		self.custom_host = custom_host
		self.custom_port = custom_port
		self.fixed_access = fixed_access
		self.access_id = access_id
		self.access_name = access_name

ACCESS_SETTINGS_SCHEMA = {
	'read': ar.Boolean(),
	'update': ar.Boolean(),
	'export': ar.Boolean(),
	'export_file': ar.Unicode(),
	'product_name': ar.Unicode(),
	'product_instance': InstanceOfProduct,
	'access_scope': ar.ScopeOfService,
	'custom_host': ar.Unicode(),
	'custom_port': ar.Integer8(),
	'fixed_access': ar.Boolean(),
	'access_id': ar.UUID(),
	'access_name': ar.Unicode(),
}

ar.bind(AccessSettings, object_schema=ACCESS_SETTINGS_SCHEMA)

#
#
def procedure_access(self, access):
	settings = ar.object_custom_settings()
	cloud_ip = settings.cloud_ip
	login_token = settings.login_token

	crud = sum([access.read, access.update, access.export])

	f = crud_address_and_token(crud, cloud_ip, login_token)
	if f:
		return f

	if access.product_name or access.product_instance or access.custom_host or access.custom_port or access.access_scope or access.fixed_access:
		if access.product_name and access.product_instance:
			if access.custom_host and access.custom_port:
				access_ipp = ar.HostPort(access.custom_host, access.custom_port)
			elif access.custom_host or access.custom_port:
				f = ar.Faulted('need both custom host and custom port', 'use --custom-host=10.1.4.27 --custom-port=40100')
				return f
			elif access.access_scope == ar.ScopeOfService.HOST:
				access_ipp = ar.HostPort('127.0.0.1', 32177)
			elif access.access_scope == ar.ScopeOfService.LAN:
				access_ipp = ar.HostPort('192.168.1.176', 32177)
			else:
				f = ar.Faulted('need an access scope of HOST or LAN', 'use --access-scope=LAN')
				return f
			product = ProductAccess(access_ipp=access_ipp,
				product_name=access.product_name, product_instance=access.product_instance)
			f = output_access(product, access.export_file)
			if f:
				return f
			return None
		elif access.product_name or access.product_instance:
			f = ar.Faulted('need both product name and product instance', 'use --product-name=Unicorn --product-instance=PRODUCTION')
			return f
		elif access.fixed_access:
			if access.custom_host and access.custom_port:
				access_ipp = ar.HostPort(access.custom_host, access.custom_port)
			elif access.custom_host or access.custom_port:
				f = ar.Faulted('need both custom host and custom port', 'use --custom-host=10.1.4.27 --custom-port=40100')
				return f
			elif access.access_scope == ar.ScopeOfService.HOST:
				access_ipp = ar.HostPort('127.0.0.1', 32176)
			elif access.access_scope == ar.ScopeOfService.LAN:
				access_ipp = ar.HostPort('192.168.1.176', 32176)
			else:
				f = ar.Faulted('need an access scope of HOST or LAN', 'use --access-scope=LAN')
				return f
			f = output_access(access_ipp, access.export_file)
			if f:
				return f
		return None

	ar.connect(self, ar.HostPort(cloud_ip, FOH_PORT))
	m = self.select(ar.Connected, ar.NotConnected, ar.Stop)
	if isinstance(m, ar.Connected):
		session = self.return_address
	elif isinstance(m, ar.NotConnected):
		return m
	else:
		return ar.Aborted()

	try:
		if access.update:
			return access_update(self, login_token, session, access)
		elif access.export:
			return access_export(self, login_token, session, access)
		return access_read(self, login_token, session, access)
	finally:
		self.send(ar.Close(), session)
		self.select(ar.Closed, ar.Stop)

def access_read(self, login_token, session, access):
	read = AccessRead(login_token=login_token,
		access_id=access.access_id)
	fill_form(self, read)
	if not access.access_id:
		f = ar.Faulted('access id not specified', 'use --access-id=<uuid>')
		return f
	self.send(read, session)
	m = self.select(DirectoryAccessPage, ar.Faulted, ar.Abandoned, ar.Stop)
	if isinstance(m, DirectoryAccessPage):
		return m
	elif isinstance(m, ar.Faulted):
		return m
	elif isinstance(m, ar.Abandoned):
		f = ar.Faulted('remote abandoned connection', 'try later?')
		return f
	else:
		return ar.Aborted()
	return None

def access_update(self, login_token, session, access):
	update = AccessUpdate(login_token=login_token, access_id=access.access_id)
	fill_form(self, update)
	if not access.access_id:
		f = ar.Faulted('access id not specified', 'use --access-id=<uuid>')
		return f
	self.send(update, session)
	m = self.select(DirectoryAccessPage, ar.Faulted, ar.Abandoned, ar.Stop)
	if isinstance(m, DirectoryAccessPage):
		return m
	elif isinstance(m, ar.Faulted):
		return m
	elif isinstance(m, ar.Abandoned):
		f = ar.Faulted('remote abandoned connection', 'try later?')
		return f
	else:
		return ar.Aborted()
	return None

def output_access(access, export_file):
	if not export_file:
		try:
			encoding = ar.CodecJson(pretty_format=True)
			s = encoding.encode(access, ar.Any())
		except ar.CodecError as e:
			s = str(e)
			f = ar.Failed(encode_access=(s, None))
			return f
		ar.output_line(s)
		return None

	try:
		f = ar.File(export_file, ar.Any(), decorate_names=False)
		f.store(access)
	except (ar.FileFailure, ar.CodecError) as e:
		s = str(e)
		f = ar.Failed(encode_access_file=(s, None))
		return f
	return None

def access_export(self, login_token, session, access):
	settings = ar.object_custom_settings()
	cloud_ip = settings.cloud_ip

	export = AccessExport(login_token=login_token,
		access_id=access.access_id, access_name=access.access_name)
	fill_form(self, export)
	if not export.access_id:
		f = ar.Faulted('access id not specified', 'use --access-id=<uuid>')
		return f
	if not export.access_name:
		f = ar.Faulted('access name not specified', 'use --access-name=<uuid>')
		return f
	self.send(export, session)
	m = self.select(DirectoryAccessExported, ar.Faulted, ar.Abandoned, ar.Stop)
	if isinstance(m, DirectoryAccessExported):
		cloud_ipp = ar.HostPort(cloud_ip, FOH_PORT)
		w = WideAreaAccess(access_ipp=cloud_ipp, access_token=m.access_token,
			account_id=m.account_id, directory_id=m.directory_id)
		f = output_access(w, access.export_file)
		if f:
			return f
		return None
	elif isinstance(m, ar.Faulted):
		return m
	elif isinstance(m, ar.Abandoned):
		f = ar.Faulted('remote abandoned connection', 'try later?')
		return f
	else:
		return ar.Aborted()
	return None
