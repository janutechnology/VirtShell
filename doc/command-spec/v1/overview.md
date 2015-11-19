# VirtShell Command V1
Manage Virtual Machines and Containers via Shell's commands

Commands specification (Under Construction)

virtsh user
===========
	synopsis
	========
		virtsh user add <user> [--role <role>]
		virtsh host disable <user>
		virtsh host list

	description
	===========
		Manage the set of users that have access to virtshell.

		Examples of the options are as follows:
			role: Administrator | user

		Note:
			The default value for role is user.

	commands
	========
		- add: Adds a new user in the repository.
		- disable: Disable a user of the repository.
		- list: shows a list of existing users

virtsh host
===========
	synopsis
	========
		virtsh host add <name> [--ip | -i <ip>] <user> (<password> | [--key | -k <key>]) [--type | -t type]
		virtsh host rm <name> [--ip | -i <ip>]
		virtsh host restart <name> [--ip | -i <ip>]
		virtsh host rename <old> <new>
		virtsh host list

	description
	===========
		Manage the set of hosts ("Physical machines") whose containers or virtual machines you have.

		Examples of the options are as follows:
			key: /home/callanor/.ssh/id_rsa.pub
			type: GeneralPurpose | ComputeOptimized | MemoryOptimized | StorageOptimized

		Note:
			The default value for type is GeneralPurpose.

	commands
	========
		- add: Adds a new host machine in the repository.
		- rm: Removes a host machine of the repository.
		- restart: Restarts a remote host machine.
		- rename: Rename the machine named <old> to <new>.
		- list: shows a list of existing hosts

virtsh iso
==========
	synopsis
	========
		virtsh iso add <name> <release_version> <os> <variant> <arch> <path_iso>
		virtsh iso create <name> <release_version> <os> <variant> <arch> <timezone>] <user>
								 (<password> | [--key | -k <key>]) <preseed_file>
		virtsh iso rm <name>
		virtsh iso list

	description
	===========
		Manage the set of isos used to create new virtual machines

	commands
	========
		- add: Adds a new iso in the repository.
		- create: Creates a new iso in the repository using a predefined preseed file.
			   Examples of the options are as follows:
			   		name: ubuntu_server_14.04.2_amd64 
					release_version: 14.04.2 
					os: ubuntu 
					variant: (server/desktop) 
					arch: (i386/amd64) 
					timezone: America/Bogota 
					user: janu 
					password: janu 
					key: /home/callanor/.ssh/id_rsa.pub
					preseed_file: /home/callanor/seed_file.txt
		- rm: Removes a iso of the repository.
		- list: shows a list of existing isos

virtsh container-template
=========================
	synopsis
	========
		virtsh container-template add <name> <os> <arch> <release> (<url> | <path_image>)
		virtsh container-template rm <name>
		virtsh container-template list

	description
	===========
		Manage the set of container templates used to create new containers.

	commands
	========
		- add: Adds a new image in the repository.
			   Examples of options are as follow:
					name: ubuntu 
					os: ubuntu 
					arch: 64 
					release: trusty
					url: https://gist.github.com/hagix9/3514296#file-lxc-centos
					path_image: /home/cllano/templates/my-lxc-centos
		- rm: Removes a image of the repository.
		- list: shows a list of existing container templates

virtsh provisioner
==================
	synopsis
	========
		virtsh provisioner upload <name> <path_script> [--howtorun <way_of_execution>] [--files | -f <path_files>]
								         [--tag <tag>] [--dependencies <[dependency(ies) of other containers o vmchacines]>]
		virtsh provisioner execute <provisioner_name> <instance_name>
		virtsh provisioner rm <name>
		virtsh provisioner list

	description
	===========
		Manage the set of provisioners scripts or programs used to provisioning containers or virtual machines.

	commands
	========
		- upload: Adds a new provisioner in the repository.
			Examples of options are as follows:
				path_script: /home/callanor/scripts/path.sh
				howtorun: source (or java or python or sh, any command)
				files: /home/callanor/files
				tag: backend (Type of Provisioner)
				dependencies: [db-users, db-transaccional]
		- execute: Lets you run execute a provisioning script in an instance
		- rm: Removes a provisioner of the repository.
		- list: shows a list of existing provisioners.

virtsh instance
===============
	synopsis
	========
		virtsh instance create <name> [--provisioner | -p <provisioner_name>] [--memory | -m <amount>] 
									[--launch | -l <amount>] [--cpus | -c <amount>] [--hdsize | -h <amount>] [--vars | -v <provisioning_variables>] [--host_type <host_type>] [--drive | -d <drive>] [--container_template | -t <template_name>] [--iso | -i <iso_name>]
		virtsh instance start <name>
		virtsh instance stop <name>
		virtsh instance restart <name>
		virtsh instance destroy <name>
		virtsh instance clone <name> <new_name>
		virtsh instance list

	description
	===========
		Manage to set of instances of the different hosts.

	commands
	========
		- create: Creates a new instance in a host.
				Examples of options are as follow:
					provisioner: transactional_log 
					launch: 1:3 the value default is 1 (Min:Max)
					memory:1024
					cpus:2
					hdsize:2GB
					vars: /home/callanor/variables/variables.yaml (Dictionary key:value in yaml format)
						Examples:
							url : hotmail.com
							ip : 192.168.56.103
							user : my_user
							password : my_password
					template_name: centos_6.5
					iso: ubuntu_server_14.04.2_amd64 
					host_type: GeneralPurpose the default value is GeneralPurpose
					drive: lxc, virtualbox, vmware, ec2, kvm
		- start: Starts a instance
		- stop: Stops a instance
		- restart: Restarts a instance
		- destroy: Destroys a instance
		- clone: Clone a instance
		- list: shows a list of existing instances

virtsh execute
==============
	synopsis
	========
		virtsh execute <command(s)> ([<instance_name(s)>] | [--ip | -i <ip(s)>] | [--type <type>] | [--tag <tag>])

	description
	===========
		The virtsh execute utility allows you Execute one or more commands in the instances.
		e.g:
			virtsh execute "uname -r"  Llano001 Llano002
			virtsh execute "uname -r" Llano00[1-2]
			virtsh execute "apt-get -y install mc" --type db
			virtsh execute "yum -y install httpd" --tag web Llano001

virtsh package
==============
	synopsis
	========
		virtsh package <option> <package(s)> ([<instance_name(s)>] | [--ip | -i <ip(s)>] | [--type <type>] | [--tag <tag>])

	description
	===========
		The virtsh package utility allows you to do functions as installation of new software packages, upgrade of existing software packages, updating of the package list index, and even upgrading the entire system.

		packages may be an single software packages or many packages separated for the blank space character equal that
		linux. By default -y for unattended-upgrades package.

		Note:
			<option>: 
				-i install new software packages
				-u upgrade software packages
				-r remove software packages
		e.g:
			virtsh package -i package1 package2 package3 Llano001 Llano002
			virtsh package -i package1 pacakge2 package3 Llano00[1-2] 
			virtsh package -i package1 --tag db 

virtsh show
============
	synopsis
	========
		virtsh show <category_property> <property_name> ([<name(s)>] | [--ip | -i <ip(s)>] | [--tag <tag>])

	description
	===========
		The virtsh show utility allows you to get information of properties exposed of the entire system or of devices.

	Categories and properties:
	=========================
		- network
			- ip (ipv4 and ipv6)
			- gateway
			- mask
			- interfaces (show all interfaces with your information)
		- system
			- total_memory
			- swap
			- cpu (cpu usage)
			- process (summary of process, total, running, stuck, sleeping, threads)

		e.g:
			virtsh show network ip Llano001 Llano002
			virtsh show network gateway Llano00[1-2]
			virtsh show network gateway --type web
			virtsh show network interfaces Llano001
			virtsh show system total_memory --tag web
			virtsh show system cpu Llano002
			virtsh show system process Llano001
			virtsh show list

virtsh copy
===========
	synopsis
	========
		virtsh copy <source> <target> [--owner <owner>] [--group <group>] [--mode <mode>]
					([<name(s)>] | [--ip | -i <ip(s)>] | [--type <type>] | [--tag <tag>])

	description
	===========
		The virtsh copy utility copies the contents of the sources files or sources directories to targets files or targets directories.

		The options are as follow: 
			--owner root 
			--group root 
			--mode 0644 

		e.g:
			virtsh copy /path/to/file/file.ext /path/to/target
			virtsh copy /path/to/file/file.ext /path/to/target --type web
			virtsh copy /path/to/directory /path/to/destination --owner root --group root --mode 0644 Llano001
			virtsh copy /path/to/directory /path/to/destination --mode 0644 Llano001 Llano002
			virtsh copy /path/to/directory /path/to/destination Llano00[1-2]
 
virtsh file
===========
	synopsis
	========
		virtsh file <name> --action <action> --content <content> [--owner <owner>] [--group <group>] [--mode <mode>] 
						   ([<nam[--owner <owner>] [--group <group>] [--mode <mode>] e(s)>] | 
						    [--ip | -i <ip(s)>] | [--type <type>] | [--tag <tag>])

	description
	===========
		The virtsh file utility allows you to create, overwrite or add content inside of a file.

		The options are as follow:
			--action create | append | overwrite | delete
			--owner root 
			--group root 
			--mode 0644 
			--content "PATH  DEFAULT="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/var/alertlogic/bin