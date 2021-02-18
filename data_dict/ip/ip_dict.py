import os
import pathlib
from datetime import datetime

from markdown import markdown
from markupsafe import Markup

from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('ip', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'ip'
information = {
	'tool': 'IP',
	'title': 'IP',
	'subtitle': 'This site is a reference for IPv4 and IPv6',
	'description': 'The Internet Protocol (IP) currently resides at v4 and is moving towards v6 - and has been for decades. IP is the principal communications protocol for interconnected devices and established the Internet. IP has the tasks of delivering packets from the source to a host destination. At the current rate IPv6 will be fully implemented by 2148. The reasons for the slow gradual adoption is associated with expensive transistioning costs.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'state': '❌',
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'IP',
			[
				helper.characteristics.get('standard'),
			])
	],
	'topic_uris': [
		'standard',
	],

}
general_info_text = 'Worth Knowing about IPv4'
general_info_text_lead = 'Address Space'
general_info_links = {}
general_info = [
	Markup(markdown('The Internet is running out of IPv4 addresses and have been for decades. To combat this decade old problem IPv6 was introduced back in 1995. IPv4 has a maximum of 32^2 (32-bit) addresses (approximately 4 billion) and as you know we are about 6 billion people on the Earth. ')),
	Markup(markdown(
		'With the introduction of IPv6 the address-space grew by an ufathomable amount and will properly be around when we reach the status of a fully intergalactive species. The address space of IPv6 is 128-bit; don\'t get fooled by the 4x - that is around 340 trillion trillion trillion IP addresses (1,329,227,995,784,910,000,000,000,000,000,000,000) which is among other things, one of the reasons IPv6 addresses uses base-16 (hex notation).')),
]
general_info_flag = True
see_also = [
	{
	},
]

cheatsheet = [
	{
		'heading':helper.set_folder('Glossary'),
		'subtitle': 'Terminology',
		'description': 'Terms important to the Internet Protocol',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '86bd35b5e2ea4eed85b9f22ea13ca66c',
		'content': {
			'descriptor': [
				'Term',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9e715ca489704c28aab11cea34b455ce')[0]),
					'flag': helper.set_entry_command_string("CIDR"),

					'description': Markup('Classless interdomain routing. Developed to provide more granularity than legacy classful addressing; CIDR notation is expressed as /##'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f58b54fa010c471d900f98a1372d2a34')[0]),
					'flag': helper.set_entry_command_string("DHCP"),

					'description': Markup('Used on subnets to dynamically (and temporarily) allocate IP addresses. IPv6 uses DHCPv6'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cca224d4a89445d1b43be9374721e60e')[0]),
					'flag': helper.set_entry_command_string("ICMP"),

					'description': Markup('Internet Control Message Protocol - aka. "ping". Is used for error reporting between routers. The IPv6 version is named accordingly: ICMPv6'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('84a86b3b0d53403b8373cab3faed1c75')[0]),
					'flag': helper.set_entry_command_string("Packet"),

					'description': Markup('A packet is a quantity of bytes send from a device to another. It has address and sender fields which is why it is a neat analogy'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('648fbd0f96cb4301ac5d5819e8739b1e')[0]),
					'flag': helper.set_entry_command_string("Address Exhaustion"),

					'description': Markup('A term used when talking about IPv4\'s limited address space. It is countered by the enourmous address space introduced with IPv6'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4b9785a9140e440f8ea841814323b285')[0]),
					'flag': helper.set_entry_command_string("IGMP"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0e76627c3ff74aaebcb0703c19e63643')[0]),
					'flag': helper.set_entry_command_string("IPsec"),

					'description': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e69f0c21427b43159c54c8a8142d23b1')[0]),
					'flag': helper.set_entry_command_string("OSI"),

					'description': Markup('Open Systems Interconnection. A conceptual model that characterises the communication protocols in telecommunication'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6b618579b7484af2ae9625e65bc099a1')[0]),
					'flag': helper.set_entry_command_string("Internet Layer"),

					'description': Markup('The layer at which IP packets reside. It sits at layer 4 in the OSI model'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Classful Ranges IPv4'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '0f7f729fdfb84e05905100e5f0b72eea',
		'content': {
			'descriptor': [
				'Term',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('20f073b71bdb4f54adc52ffc7406ab06')[0]),
					'flag': helper.set_entry_command_string("A"),

					'description': Markup('0.0.0.0 – 127.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2263131475274d4289554b228e4eb252')[0]),
					'flag': helper.set_entry_command_string("B"),

					'description': Markup('128.0.0.0 - 191.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a0c12a5cbbd247aab3f4e6a255a55eb0')[0]),
					'flag': helper.set_entry_command_string("C"),

					'description': Markup('192.0.0.0 - 223.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('47b43c47cf8b4d1db4bbc7059fb264ba')[0]),
					'flag': helper.set_entry_command_string("D"),

					'description': Markup('224.0.0.0 - 239.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7d91c514aa2841e79ccb7022048cfe21')[0]),
					'flag': helper.set_entry_command_string("E"),

					'description': Markup('240.0.0.0 - 255.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('Reserved Ranges IPv4'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '0f336c7f2eda4bdba6fc5603c7b87d60',
		'content': {
			'descriptor': [
				'Reserved',
				'Range'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('1c3bb5be635248969cf7969f80f09c3b')[0]),
					'flag': helper.set_entry_command_string("Localhost"),

					'description': Markup('127.0.0.0 - 127.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a3936b4ba79547758cdbc657f41dceac')[0]),
					'flag': helper.set_entry_command_string("RFC 1918"),

					'description': Markup('10.0.0.0 - 10.255.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f88a2a7833744b5bbdee98e7d8bbeddd')[0]),
					'flag': helper.set_entry_command_string("RFC 1918"),

					'description': Markup('172.16.0.0 - 172.31.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d5b1a0731f9e4b838a5207ff00d2a4a6')[0]),
					'flag': helper.set_entry_command_string("RFC 1918"),

					'description': Markup('192.168.0.0 - 192.168.255.255'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('IPv4 Subnetting'),
		'subtitle': 'Subnets and Subnetmasking',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '983aa230d12046a388c1fb287543b937',
		'content': {
			'descriptor': [
				'Subnet',
				'Addresses'
				'Netmask'
			],
			'data': [

				{
					'static_red': Markup(helper.set_entry_folder('7abe0edaea9442e6adac050b6fff3902')[0]),
					'flag': helper.set_entry_command_string("/31"),

					'addresses': Markup('2'),
					'netmask': Markup('255.255.255.254'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ad35804a4f494d6c9b5f5cb46b6e955c')[0]),
					'flag': helper.set_entry_command_string("/30"),

					'addresses': Markup('4'),
					'netmask': Markup('255.255.255.252'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('27fc33d1cda04f33bc5b2291d76e7c56')[0]),
					'flag': helper.set_entry_command_string("/29"),

					'addresses': Markup('8'),
					'netmask': Markup('255.255.255.248'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('637d934573824fa6a298c87470564c56')[0]),
					'flag': helper.set_entry_command_string("/28"),

					'addresses': Markup('16'),
					'netmask': Markup('255.255.255.240'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('50869348249641a4b04548cb1dc967bd')[0]),
					'flag': helper.set_entry_command_string("/27"),

					'addresses': Markup('32'),
					'netmask': Markup('255.255.255.224'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6d7d8e7892e64822ad1ec2fd60c7e02f')[0]),
					'flag': helper.set_entry_command_string("/26"),

					'addresses': Markup('64'),
					'netmask': Markup('255.255.255.192'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2e62fa51d3ef4899972bb436a2b78163')[0]),
					'flag': helper.set_entry_command_string("/25"),

					'addresses': Markup('128'),
					'netmask': Markup('255.255.255.128'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('943adca597ed48108131ae5f33837139')[0]),
					'flag': helper.set_entry_command_string("/24"),

					'addresses': Markup('256'),
					'netmask': Markup('255.255.255.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('3a1726c8430142f9a6a6d4f6d1c3be2c')[0]),
					'flag': helper.set_entry_command_string("/23"),

					'addresses': Markup('512'),
					'netmask': Markup('255.255.254.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('34f7ab42499e40cca31e43ae668cf118')[0]),
					'flag': helper.set_entry_command_string("/22"),

					'addresses': Markup('1024'),
					'netmask': Markup('255.255.252.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1adaa98ef17844a4834f59e927824ccf')[0]),
					'flag': helper.set_entry_command_string("/21"),

					'addresses': Markup('2048'),
					'netmask': Markup('255.255.248.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4a38a12dccf24baca7958d7a7fa1040d')[0]),
					'flag': helper.set_entry_command_string("/20"),

					'addresses': Markup('4096'),
					'netmask': Markup('255.255.240.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('dd7f072319cd4a54a2e3f591c64f7ce8')[0]),
					'flag': helper.set_entry_command_string("/19"),

					'addresses': Markup('8192'),
					'netmask': Markup('255.255.224.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('eed567406aee46d7911f03a244d82bfe')[0]),
					'flag': helper.set_entry_command_string("/18"),

					'addresses': Markup('16384'),
					'netmask': Markup('255.255.192.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4caa65db10bc4d2283bdcba442c99042')[0]),
					'flag': helper.set_entry_command_string("/17"),

					'addresses': Markup('32768'),
					'netmask': Markup('255.255.128.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('19506f4d14dd46af8d77300b56272a9f')[0]),
					'flag': helper.set_entry_command_string("/16"),

					'addresses': Markup('65536'),
					'netmask': Markup('255.255.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7cc9bd6ccaa24ce799952fa80f86f909')[0]),
					'flag': helper.set_entry_command_string("/15"),

					'addresses': Markup('131072'),
					'netmask': Markup('255.254.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2a85d83d82e04b2296b06aef82f90f38')[0]),
					'flag': helper.set_entry_command_string("/14"),

					'addresses': Markup('262144'),
					'netmask': Markup('255.252.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f0ec1b5d83654e749cf2f306830ea53b')[0]),
					'flag': helper.set_entry_command_string("/13"),

					'addresses': Markup('524288'),
					'netmask': Markup('255.248.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cdd35b9346e84411a7e68d1fa60db4e6')[0]),
					'flag': helper.set_entry_command_string("/12"),

					'addresses': Markup('1048576'),
					'netmask': Markup('255.240.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('491b54bed26540eda47747da57ffeba9')[0]),
					'flag': helper.set_entry_command_string("/11"),

					'addresses': Markup('2097152'),
					'netmask': Markup('255.224.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a0f53aee26d14b0a9aae97add55d76a7')[0]),
					'flag': helper.set_entry_command_string("/10"),

					'addresses': Markup('4194304'),
					'netmask': Markup('255.192.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7707834d19734bacbf28037fe15b19c5')[0]),
					'flag': helper.set_entry_command_string("/9"),

					'addresses': Markup('8388608'),
					'netmask': Markup('255.128.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e9c838bb5d8143028d9a80c3ae43dcfe')[0]),
					'flag': helper.set_entry_command_string("/8"),

					'addresses': Markup('16777216'),
					'netmask': Markup('255.0.0.0'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
			]
		}
	},
	{
		'heading':helper.set_folder('IPv6 Subnetting'),
		'subtitle': 'Subnets and Subnetmasking',
		'description': '',
		'columns': 'col-lg-12 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '85d09dc143ee4054b48a5a4e5b4a52a3',
		'content': {
			'descriptor': [
				'Subnet',
				'Addresses'
				'Amount of a /64'
			],
			'data': [

				{
					'static_red': Markup(helper.set_entry_folder('7ee62e9cbb8b4776b8c064cad7923e53')[0]),
					'flag': helper.set_entry_command_string("/128"),

					'addresses': Markup('1'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('50dbe40a563f4183b32e96222ab7798a')[0]),
					'flag': helper.set_entry_command_string("/127"),

					'addresses': Markup('2'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0733d217288540728ba123a4b38284d2')[0]),
					'flag': helper.set_entry_command_string("/126"),

					'addresses': Markup('4'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('29d4b4f9957e4a248b193b1c91f66b4c')[0]),
					'flag': helper.set_entry_command_string("/125"),

					'addresses': Markup('8'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('9545b63ba2e447afbe8f0d974ce8ccb2')[0]),
					'flag': helper.set_entry_command_string("/124"),

					'addresses': Markup('16'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('834396f49fad40eabe097425d4bdb195')[0]),
					'flag': helper.set_entry_command_string("/123"),

					'addresses': Markup('32'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a13f6448a2c44691ab0ac219ef134c03')[0]),
					'flag': helper.set_entry_command_string("/122"),

					'addresses': Markup('64'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('30c7f28647f54bc18ae2c10f75b4072e')[0]),
					'flag': helper.set_entry_command_string("/121"),

					'addresses': Markup('128'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('857a4af7b60340a2ace00eee440c4eb1')[0]),
					'flag': helper.set_entry_command_string("/120"),

					'addresses': Markup('256'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('45ac6e1135a54ffd8c092ed84a8622ee')[0]),
					'flag': helper.set_entry_command_string("/119"),

					'addresses': Markup('512'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('fdf9639e4c5e40c2965b61b731e12f29')[0]),
					'flag': helper.set_entry_command_string("/118"),

					'addresses': Markup('1,024'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7e6c018bc3024452a617bc7716baf096')[0]),
					'flag': helper.set_entry_command_string("/117"),

					'addresses': Markup('2,048'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1fbccd3524f04027a84a89f36bf54767')[0]),
					'flag': helper.set_entry_command_string("/116"),

					'addresses': Markup('4,096'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('3fb9a1bc4d3e4a60bf7d5e97d8ce04a3')[0]),
					'flag': helper.set_entry_command_string("/115"),

					'addresses': Markup('8,192'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('866dd4b62d404e4a82e9bd655faf8f0b')[0]),
					'flag': helper.set_entry_command_string("/114"),

					'addresses': Markup('16,384'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a387b0e620e74d7d946fdb6a8f3ee466')[0]),
					'flag': helper.set_entry_command_string("/113"),

					'addresses': Markup('32,768'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c4075d298a694e8287333badecdecfb3')[0]),
					'flag': helper.set_entry_command_string("/112"),

					'addresses': Markup('65,536'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('66799c874ef340c096c2ae4469f08bf8')[0]),
					'flag': helper.set_entry_command_string("/111"),

					'addresses': Markup('131,072'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1c46cd7f5a514335b43a71861986eaa2')[0]),
					'flag': helper.set_entry_command_string("/110"),

					'addresses': Markup('262,144'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2aa6f609e18c4c11afde88dc9dd725da')[0]),
					'flag': helper.set_entry_command_string("/109"),

					'addresses': Markup('524,288'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('051f65929ba746f9b4c1c7af41583934')[0]),
					'flag': helper.set_entry_command_string("/108"),

					'addresses': Markup('1,048,576'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2246af6271ab47dc9d8ce547fe1afdc5')[0]),
					'flag': helper.set_entry_command_string("/107"),

					'addresses': Markup('2,097,152'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('341e15b24f764fd2977356b9a002e516')[0]),
					'flag': helper.set_entry_command_string("/106"),

					'addresses': Markup('4,194,304'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6cd99850f57743b384b4ebd5dd3fbbe9')[0]),
					'flag': helper.set_entry_command_string("/105"),

					'addresses': Markup('8,388,608'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ef388cb095a447c78d51fa752c156349')[0]),
					'flag': helper.set_entry_command_string("/104"),

					'addresses': Markup('16,777,216'),
					'amount': Markup('This is equivalent to an IPv4 Internet or IPv4 /8'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('06009319524e41948cfcd56bac495517')[0]),
					'flag': helper.set_entry_command_string("/103"),

					'addresses': Markup('33,554,432'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5b44b52d1a6848e59f415eed5fa40374')[0]),
					'flag': helper.set_entry_command_string("/102"),

					'addresses': Markup('67,108,864'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('955f83a2bf9e4121ac42531d95af796b')[0]),
					'flag': helper.set_entry_command_string("/101"),

					'addresses': Markup('134,217,728'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2858203dd7a940bba39629a821e38d09')[0]),
					'flag': helper.set_entry_command_string("/100"),

					'addresses': Markup('268,435,456'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5082c3cf27ab499dbc1106a3a6e467ef')[0]),
					'flag': helper.set_entry_command_string("/99"),

					'addresses': Markup('536,870,912'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5f0b000f3e39450384fd86662a081133')[0]),
					'flag': helper.set_entry_command_string("/98"),

					'addresses': Markup('1,073,741,824'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ad4792539e9d43fab0169237b119d350')[0]),
					'flag': helper.set_entry_command_string("/97"),

					'addresses': Markup('2,147,483,648'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('3c9434e4ef454267943c7d3c6a9d0a91')[0]),
					'flag': helper.set_entry_command_string("/96"),

					'addresses': Markup('4,294,967,296'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('8aa8dc4cba6946e0959e6ca74b2448a2')[0]),
					'flag': helper.set_entry_command_string("/95"),

					'addresses': Markup('8,589,934,592'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7956024eaf47463fb3fa2d65504acedb')[0]),
					'flag': helper.set_entry_command_string("/94"),

					'addresses': Markup('17,179,869,184'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('86bc92f2f952450aa1c4e7b6a3ed667a')[0]),
					'flag': helper.set_entry_command_string("/93"),

					'addresses': Markup('34,359,738,368'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4cbb218be3924816be380c0fd8656037')[0]),
					'flag': helper.set_entry_command_string("/92"),

					'addresses': Markup('68,719,476,736'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0f8f3ad776ef4e2cb6b00999ba487851')[0]),
					'flag': helper.set_entry_command_string("/91"),

					'addresses': Markup('137,438,953,472'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f60671c9b1554ce6a79367b6bd0590b7')[0]),
					'flag': helper.set_entry_command_string("/90"),

					'addresses': Markup('274,877,906,944'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bcc6bc8df6eb43569d7e72dbf094b98d')[0]),
					'flag': helper.set_entry_command_string("/89"),

					'addresses': Markup('549,755,813,888'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bc241393ab80493f89fd22b0653d233e')[0]),
					'flag': helper.set_entry_command_string("/88"),

					'addresses': Markup('1,099,511,627,776'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ffd7534713284f208bbe33c286a0c87f')[0]),
					'flag': helper.set_entry_command_string("/87"),

					'addresses': Markup('2,199,023,255,552'),
					'amount': Markup('1/8,388,608'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('28190ac877054fd6b38740ab872e79d5')[0]),
					'flag': helper.set_entry_command_string("/86"),

					'addresses': Markup('4,398,046,511,104'),
					'amount': Markup('1/4,194,304'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b68d6c3226a84d48b57734c6a0b72853')[0]),
					'flag': helper.set_entry_command_string("/85"),

					'addresses': Markup('8,796,093,022,208'),
					'amount': Markup('1/2,097,152'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('660de664c0eb4fbeb44e25d3c515665f')[0]),
					'flag': helper.set_entry_command_string("/84"),

					'addresses': Markup('17,592,186,044,416'),
					'amount': Markup('1/1,048,576'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('fe29ac7579fc4b2893d246a58d27c612')[0]),
					'flag': helper.set_entry_command_string("/83"),

					'addresses': Markup('35,184,372,088,832'),
					'amount': Markup('1/524,288'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4b135498b1cf450b85d5f51c7188dda0')[0]),
					'flag': helper.set_entry_command_string("/82"),

					'addresses': Markup('70,368,744,177,664'),
					'amount': Markup('1/262,144'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('92267fa874734c5e867cfbca9e298ef2')[0]),
					'flag': helper.set_entry_command_string("/81"),

					'addresses': Markup('140,737,488,355,328'),
					'amount': Markup('1/131,072'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ebcc961543fd480687e8d76f6d0bd110')[0]),
					'flag': helper.set_entry_command_string("/80"),

					'addresses': Markup('281,474,976,710,656'),
					'amount': Markup('1/65,536'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e6210dfd03ca48eda3436d9a2d4d131b')[0]),
					'flag': helper.set_entry_command_string("/79"),

					'addresses': Markup('562,949,953,421,312'),
					'amount': Markup('1/32,768'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c622e0ff14ff4015b8e52b0364223e98')[0]),
					'flag': helper.set_entry_command_string("/78"),

					'addresses': Markup('1,125,899,906,842,620'),
					'amount': Markup('1/16,384'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b5f9ac09030a4c3285b6cd8366b416e8')[0]),
					'flag': helper.set_entry_command_string("/77"),

					'addresses': Markup('2,251,799,813,685,240'),
					'amount': Markup('1/8,192'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('dbb192fd8035430182b7ad6ec24737c1')[0]),
					'flag': helper.set_entry_command_string("/76"),

					'addresses': Markup('4,503,599,627,370,490'),
					'amount': Markup('1/4,096'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a71988b20af646d2a5a3def2ed42d5c2')[0]),
					'flag': helper.set_entry_command_string("/75"),

					'addresses': Markup('9,007,199,254,740,990'),
					'amount': Markup('1/2,048'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e6ab485a43ea416093804185589281e5')[0]),
					'flag': helper.set_entry_command_string("/74"),

					'addresses': Markup('18,014,398,509,481,900'),
					'amount': Markup('1/1,024'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ba509be183c847a49e225138eb2ae10a')[0]),
					'flag': helper.set_entry_command_string("/73"),

					'addresses': Markup('36,028,797,018,963,900'),
					'amount': Markup('1/512'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('94e8dbc857fd4edc982de254180658c8')[0]),
					'flag': helper.set_entry_command_string("/72"),

					'addresses': Markup('72,057,594,037,927,900'),
					'amount': Markup('1/256'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('83e62dbc16ae40299f6f2de9639ae96c')[0]),
					'flag': helper.set_entry_command_string("/71"),

					'addresses': Markup('144,115,188,075,855,000'),
					'amount': Markup('1/128'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('384bc6cac33d4c308a1079ada01415fa')[0]),
					'flag': helper.set_entry_command_string("/70"),

					'addresses': Markup('288,230,376,151,711,000'),
					'amount': Markup('1/64'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f165b54c20cd4568a8e91fff92e414ae')[0]),
					'flag': helper.set_entry_command_string("/69"),

					'addresses': Markup('576,460,752,303,423,000'),
					'amount': Markup('1/32'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7e8ef07db7dc446cb3a7206223bc48d4')[0]),
					'flag': helper.set_entry_command_string("/68"),

					'addresses': Markup('1,152,921,504,606,840,000'),
					'amount': Markup('1/16'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bd395d361cf74c238dfa5af8559decc6')[0]),
					'flag': helper.set_entry_command_string("/67"),

					'addresses': Markup('2,305,843,009,213,690,000'),
					'amount': Markup('1/8'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7860dd274838442cb9eb0a984f4be714')[0]),
					'flag': helper.set_entry_command_string("/66"),

					'addresses': Markup('4,611,686,018,427,380,000'),
					'amount': Markup('1/4'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ff760a60e2e64c1a8b55b3668b7730fc')[0]),
					'flag': helper.set_entry_command_string("/65"),

					'addresses': Markup('9,223,372,036,854,770,000'),
					'amount': Markup('1/2'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b5252768b6a3404e8928b64f70d4e3f9')[0]),
					'flag': helper.set_entry_command_string("/64"),

					'addresses': Markup('18,446,744,073,709,500,000'),
					'amount': Markup('This is the standard end user allocation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e04274bd005646d1aab57271ae8c29d2')[0]),
					'flag': helper.set_entry_command_string("/63"),

					'addresses': Markup('36,893,488,147,419,100,000'),
					'amount': Markup('2'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('20a4e2155ce34bd4995b48ff0f71af54')[0]),
					'flag': helper.set_entry_command_string("/62"),

					'addresses': Markup('73,786,976,294,838,200,000'),
					'amount': Markup('4'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('9b25c01a8ac241f7b031b97b7ab2f952')[0]),
					'flag': helper.set_entry_command_string("/61"),

					'addresses': Markup('147,573,952,589,676,000,000'),
					'amount': Markup('8'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('dbbc078eb04e40ada5b89bce2d979e90')[0]),
					'flag': helper.set_entry_command_string("/60"),

					'addresses': Markup('295,147,905,179,352,000,000'),
					'amount': Markup('16'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cf953a9943fa46389177e7ef481a95d8')[0]),
					'flag': helper.set_entry_command_string("/59"),

					'addresses': Markup('590,295,810,358,705,000,000'),
					'amount': Markup('32'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bbeea2f9d4b7430f8586aa1194827a08')[0]),
					'flag': helper.set_entry_command_string("/58"),

					'addresses': Markup('1,180,591,620,717,410,000,000'),
					'amount': Markup('64'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('13e82cdbdb0f44c5936a2fdf1e564d99')[0]),
					'flag': helper.set_entry_command_string("/57"),

					'addresses': Markup('2,361,183,241,434,820,000,000'),
					'amount': Markup('128'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('011570e830e44a83ae055cc12a649223')[0]),
					'flag': helper.set_entry_command_string("/56"),

					'addresses': Markup('4,722,366,482,869,640,000,000'),
					'amount': Markup('256'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('436503b5d5f9459996b249d08644bf03')[0]),
					'flag': helper.set_entry_command_string("/55"),

					'addresses': Markup('9,444,732,965,739,290,000,000'),
					'amount': Markup('512'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ba2d120fbcc248cd8067b9c12588f2a2')[0]),
					'flag': helper.set_entry_command_string("/54"),

					'addresses': Markup('18,889,465,931,478,500,000,000'),
					'amount': Markup('1,024'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ba4c2862d22a4a21b6221afd013b879e')[0]),
					'flag': helper.set_entry_command_string("/53"),

					'addresses': Markup('37,778,931,862,957,100,000,000'),
					'amount': Markup('2,048'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7f241ed91cb64c82a54d4d1ae667fdb4')[0]),
					'flag': helper.set_entry_command_string("/52"),

					'addresses': Markup('75,557,863,725,914,300,000,000'),
					'amount': Markup('4,096'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ef4643a9814248d788b102e0eb769461')[0]),
					'flag': helper.set_entry_command_string("/51"),

					'addresses': Markup('151,115,727,451,828,000,000,000'),
					'amount': Markup('8,192'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b0ff2552b3134f8da0a006ed79d48f2e')[0]),
					'flag': helper.set_entry_command_string("/50"),

					'addresses': Markup('302,231,454,903,657,000,000,000'),
					'amount': Markup('16,384'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('efb02849046040ddb750ec85c6df00c5')[0]),
					'flag': helper.set_entry_command_string("/49"),

					'addresses': Markup('604,462,909,807,314,000,000,000'),
					'amount': Markup('32,768'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4737ae14d2524f1bac3ce26065f8c795')[0]),
					'flag': helper.set_entry_command_string("/48"),

					'addresses': Markup('1,208,925,819,614,620,000,000,000'),
					'amount': Markup('65,536 This is the standard business allocation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('541f1cf12351496ebfddac6ac94f423f')[0]),
					'flag': helper.set_entry_command_string("/47"),

					'addresses': Markup('2,417,851,639,229,250,000,000,000'),
					'amount': Markup('131,072'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('b5a661267d20477bb2384a0d695431e0')[0]),
					'flag': helper.set_entry_command_string("/46"),

					'addresses': Markup('4,835,703,278,458,510,000,000,000'),
					'amount': Markup('262,144'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e8f83d7c094544f5bf8be4ffbff735ec')[0]),
					'flag': helper.set_entry_command_string("/45"),

					'addresses': Markup('9,671,406,556,917,030,000,000,000'),
					'amount': Markup('524,288'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0a5bdcf301704c1a88b4a0a83ee3b006')[0]),
					'flag': helper.set_entry_command_string("/44"),

					'addresses': Markup('19,342,813,113,834,000,000,000,000'),
					'amount': Markup('1,048,576'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('20bb83547c9f48f5a9f90b8d2947adea')[0]),
					'flag': helper.set_entry_command_string("/43"),

					'addresses': Markup('38,685,626,227,668,100,000,000,000'),
					'amount': Markup('2,097,152'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('4ff3573d17f1473995989b2c77d469c4')[0]),
					'flag': helper.set_entry_command_string("/42"),

					'addresses': Markup('77,371,252,455,336,200,000,000,000'),
					'amount': Markup('4,194,304'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6163a8670ca142d292752eff9e6d0240')[0]),
					'flag': helper.set_entry_command_string("/41"),

					'addresses': Markup('154,742,504,910,672,000,000,000,000'),
					'amount': Markup('8,388,608'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('d8f9fe914a5846769325ee388083f2ac')[0]),
					'flag': helper.set_entry_command_string("/40"),

					'addresses': Markup('309,485,009,821,345,000,000,000,000'),
					'amount': Markup('16,777,216'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('cb4e4b032b934245b95785856455d231')[0]),
					'flag': helper.set_entry_command_string("/39"),

					'addresses': Markup('618,970,019,642,690,000,000,000,000'),
					'amount': Markup('33,554,432'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bf7c35a209e34102a25317538fcfabc7')[0]),
					'flag': helper.set_entry_command_string("/38"),

					'addresses': Markup('1,237,940,039,285,380,000,000,000,000'),
					'amount': Markup('67,108,864'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('6559119d5de14be1a197243a54636cc5')[0]),
					'flag': helper.set_entry_command_string("/37"),

					'addresses': Markup('2,475,880,078,570,760,000,000,000,000'),
					'amount': Markup('134,217,728'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('dd739ac1eed541b2970c2de514f54515')[0]),
					'flag': helper.set_entry_command_string("/36"),

					'addresses': Markup('4,951,760,157,141,520,000,000,000,000'),
					'amount': Markup('268,435,456'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('be6cd2defbf14365817cd5f2df287b79')[0]),
					'flag': helper.set_entry_command_string("/35"),

					'addresses': Markup('9,903,520,314,283,040,000,000,000,000'),
					'amount': Markup('536,870,912'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e43f3df8374f4a3bb01f240ad67ac221')[0]),
					'flag': helper.set_entry_command_string("/34"),

					'addresses': Markup('19,807,040,628,566,000,000,000,000,000'),
					'amount': Markup('1,073,741,824'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f177c22a55ee4902af669800e702f05b')[0]),
					'flag': helper.set_entry_command_string("/33"),

					'addresses': Markup('39,614,081,257,132,100,000,000,000,000'),
					'amount': Markup('2,147,483,648'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('ec4714419c4948d58885873d3af6899f')[0]),
					'flag': helper.set_entry_command_string("/32"),

					'addresses': Markup('79,228,162,514,264,300,000,000,000,000'),
					'amount': Markup('4,294,967,296 This is the standard ISP Allocation'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('2d97eb98c2194f86ad5a4e519942fff2')[0]),
					'flag': helper.set_entry_command_string("/31"),

					'addresses': Markup('158,456,325,028,528,000,000,000,000,000'),
					'amount': Markup('8,589,934,592'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7639a55924004779a75cfb94eb024a43')[0]),
					'flag': helper.set_entry_command_string("/30"),

					'addresses': Markup('316,912,650,057,057,000,000,000,000,000'),
					'amount': Markup('17,179,869,184'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('c72677ff4be543c6bf27e5e8d143a804')[0]),
					'flag': helper.set_entry_command_string("/29"),

					'addresses': Markup('633,825,300,114,114,000,000,000,000,000'),
					'amount': Markup('34,359,738,368'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('1aab96f59b3a40c5a5786839be2fc78f')[0]),
					'flag': helper.set_entry_command_string("/28"),

					'addresses': Markup('1,267,650,600,228,220,000,000,000,000,000'),
					'amount': Markup('68,719,476,736'),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('7390633617ca4a3c93d3cfe7d063bef8')[0]),
					'flag': helper.set_entry_command_string("/27"),

					'addresses': Markup('2,535,301,200,456,450,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('0d65d49424504f4ba5c1895e2281326d')[0]),
					'flag': helper.set_entry_command_string("/26"),

					'addresses': Markup('5,070,602,400,912,910,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e7b1e027b5ad46e9b729128b1857a2f9')[0]),
					'flag': helper.set_entry_command_string("/25"),

					'addresses': Markup('10,141,204,801,825,800,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('de2a2294580e4de7b524d57e79487073')[0]),
					'flag': helper.set_entry_command_string("/24"),

					'addresses': Markup('20,282,409,603,651,600,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f48037f263764246894096348e8591d2')[0]),
					'flag': helper.set_entry_command_string("/23"),

					'addresses': Markup('40,564,819,207,303,300,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a1288622356246189d9a72f363038ab0')[0]),
					'flag': helper.set_entry_command_string("/22"),

					'addresses': Markup('81,129,638,414,606,600,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('a0bb56aae9fd46fdaf6a9b0b84e46b44')[0]),
					'flag': helper.set_entry_command_string("/21"),

					'addresses': Markup('162,259,276,829,213,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('5f21a4459a3144a6a4400e96c1784d55')[0]),
					'flag': helper.set_entry_command_string("/20"),

					'addresses': Markup('324,518,553,658,426,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('900890e1635246a7890135d0509e3635')[0]),
					'flag': helper.set_entry_command_string("/19"),

					'addresses': Markup('649,037,107,316,853,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('23d7e2f518ec43cfaf64b147ea8e71c5')[0]),
					'flag': helper.set_entry_command_string("/18"),

					'addresses': Markup('1,298,074,214,633,700,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('30ba3c88215e443aa200f3333cc4cc53')[0]),
					'flag': helper.set_entry_command_string("/17"),

					'addresses': Markup('2,596,148,429,267,410,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('fcd66e9bccf44a8a842d7b128cd0d1b4')[0]),
					'flag': helper.set_entry_command_string("/16"),

					'addresses': Markup('5,192,296,858,534,820,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('118b5e2888b3459bb88f1012cb399149')[0]),
					'flag': helper.set_entry_command_string("/15"),

					'addresses': Markup('10,384,593,717,069,600,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('f9da2f764c0549a5a143196191dd7fb9')[0]),
					'flag': helper.set_entry_command_string("/14"),

					'addresses': Markup('20,769,187,434,139,300,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('006095c1bdc440a7a66bdaf3e613f80a')[0]),
					'flag': helper.set_entry_command_string("/13"),

					'addresses': Markup('41,538,374,868,278,600,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('90047d957e274a04b5a0952fc4c3cea3')[0]),
					'flag': helper.set_entry_command_string("/12"),

					'addresses': Markup('83,076,749,736,557,200,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('af5bfee620294c499193b510b9e33ac9')[0]),
					'flag': helper.set_entry_command_string("/11"),

					'addresses': Markup('166,153,499,473,114,000,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('bef7501c65c04fdba559179fbe7597e2')[0]),
					'flag': helper.set_entry_command_string("/10"),

					'addresses': Markup('332,306,998,946,228,000,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('380995f70bbc43c5b41f72388e2e10bf')[0]),
					'flag': helper.set_entry_command_string("/9"),

					'addresses': Markup('664,613,997,892,457,000,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},
				{
					'static_red': Markup(helper.set_entry_folder('e6f92af42ac9471b81a25a8b7bf2c6ba')[0]),
					'flag': helper.set_entry_command_string("/8"),

					'addresses': Markup('1,329,227,995,784,910,000,000,000,000,000,000,000'),
					'amount': Markup(''),
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),

				},

			]
		}
	},

]
resources = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'link': 'https://github.com',
			'title': 'Github',
			'description': Markup('A collection of thousands of git-repositories from individual users'),
			'footer': Markup('You properly know it'),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]
