# Fix wrong extensions on assets loading.

exec { 'Fix loaded files extensions':
    command => "sudo sed -i 's/.phpp/.php/g' wp-settings.php ",
    path    => '/usr/bin',
    cwd     => '/var/www/html'
}
