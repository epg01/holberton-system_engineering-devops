# Using Puppet, create a manifest that kills a process named killmenow.
exec {'killmenow':
path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
command => 'pkill killmenow',
}