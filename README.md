# citrom_api

A szerver alapból a 192.168.1.111 IP-n fut. (természetesen módositható, ha valakinek foglalt)
### szerver belépő adatok:

**user:** root

**jelszó:** password

### postgresql indítása:
```sh
service postgresql start
```
teampostgresql indítása:
```sh
cd /root/teampostgresql
sh teampostgresql-run.sh
```
(ez nem fontos, csak egy adatbázis kezelő app böngészőbe)

### teamposgresql url:
http://192.168.1.111:8082/teampostgresql/

------
### django

#### futtatás:
```sh
cd /root/citrom
python manage.py runserver 0.0.0.0:8000
```
http://192.168.1.111:8080/admin/
**név:** citrom
**jelszó:** citrompassword


update: datbázis táblák már létrehozva, de még semmi sem végleges
