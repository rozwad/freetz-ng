#!/bin/sh

. /usr/lib/libmodcgi.sh


#

sec_begin '$(lang de:"Starttyp" en:"Start type")'

cgi_print_radiogroup_service_starttype "enabled" "$PYLOAD_ENABLED" "" "" 0

sec_end

#

pyweb="$(sed -n '/^webinterface -/{N;N;N;N;N;N;N;N;N;s/.*"Activated" = \([a-zA-Z]*\).*/\1/p}' /mod/pyload/pyload.conf 2>/dev/null)"
if [ "$pyweb" == "True" -a "$(/etc/init.d/rc.pyload status)" == "running" ]; then
sec_begin '$(lang de:"Anzeigen" en:"Show")'

cat << EOF
<ul>
<li><a href="/cgi-bin/pyload" target="_blank">$(lang de:"pyLoad Webinterface" en:"pyLoad web interface")</a></li>
</ul>
EOF

sec_end
fi

#

sec_begin '$(lang de:"Konfiguration" en:"Configuration")'

cgi_print_textline_p "configdir" "$PYLOAD_CONFIGDIR" 55/255 "$(lang de:"pyLoad Verzeichnis" en:"pyLoad directory"): "

sec_end

#

if [ ! -e /mod/pyload/pyload.conf ]; then
sec_begin '$(lang de:"Erstmalige Einrichtung" en:"Initial setup")'

cat << EOF
$(lang de:"pyLoad wurde noch nicht konfiguriert. Dazu bitte diesen Befehl in einem Terminal ausf&uuml;hren" en:"pyLoad is not configured. To do so, please run this in a terminal"):<br>rc.pyload setup
EOF

sec_end
fi
