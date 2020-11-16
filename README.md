# Data-export-with-phpIPAM-API

Exporting data using phpIPAM API, converting to CSV format and writing to the file

<b>Installing Requirements</b>
<ul>
	<li>
		<b>Python 2</b>
		<ul>
			<li>
				<b>CentOS</b>
				<ul>
					<li>
						yum install -y python2
					</li>
					<li>
						pip2 install requests
					</li>
				</ul>
			</li>
			<li>
				<b>Ubuntu/Debian</b>
				<ul>
					<li>
						apt-get install -y python2
					</li>
					<li>
						pip2 install requests
					</li>
				</ul>
			</li>
		</ul>
	</li>
</ul>

<ul>
	<li>
		<b>Python 3</b>
		<ul>
			<li>
				<b>CentOS</b>
				<ul>
					<li>
						yum install -y python3
					</li>
					<li>
						pip3 install requests
					</li>
				</ul>
			</li>
			<li>
				<b>Ubuntu/Debian</b>
				<ul>
					<li>
						apt-get install -y python3
					</li>
					<li>
						pip3 install requests
					</li>
				</ul>
			</li>
		</ul>
	</li>
</ul>

<b>User Token</b>
In order to make requests without encryption and SSL operations, the following information in the "config.php" file should be as shown:

<ul>
	<li>
		vi /var/www/html/phpipam/config.php
		<ul>
			<li>
				//$api_crypt_encryption_library = "mcrypt"
			</li>
			<li>
				&api_allow_unsafe = true
			</li>
		</ul>
	</li>
</ul>

API service must be opened over the interface and an API key must be created so that the "App security" information will be "User Token". Along with the APP ID information created in the API service, the server address, user name and password must be edited in the script.

<b>Usage</b>
<table>
	<tr><th>Controller Name</th><th>Description</th></tr>
	<tr><td>sections</td><td>Manages sections part of phpipam</td></tr>
	<tr><td>subnets</td><td>Manages Subnets and folder objects</td></tr>
	<tr><td>folders</td><td>Folders is alias for subnets controller.</td></tr>
	<tr><td>addresses</td><td>Manages IP addresses</td></tr>
	<tr><td>vlans</td><td>Manages VLANs</td></tr>
	<tr><td>l2domains</td><td>Manages VLAN domains</td></tr>
	<tr><td>vrfs</td><td>Manages VRF</td></tr>
	<tr><td>tools</td><td>Tools controller (special)</td></tr>
	<tr><td>prefix</td><td>Prefix controller (special)</td></tr>
	<tr><td>user/all</td><td>Returns all users 1.3 (rwa app permissions required)</td></tr>
	<tr><td>user/admins</td><td>Returns admin users 1.3 (rwa app permissions required)</td></tr>
</table>
<br>
<b>Examples</b>
<ul>
  <li>
    <b>python2/3 phpIPAM_with_user_token.py controller_name</b>
    <ul>
      <li>
        python2/3 phpIPAM_with_user_token.py addresses
      </li>
      <li>
        python2/3 phpIPAM_with_user_token.py user/all
      </li>
    </ul>
  </li>
  </ul>

