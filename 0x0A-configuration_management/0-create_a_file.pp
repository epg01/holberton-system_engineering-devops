# Create a file if it doesn't exist, and enter a character string.
file {'/tmp/holberton':
ensure  => present,
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}