#!/bin/sh
curl -v -XPOST http://localhost:8000/person/ -H "Authorization: Bearer $(curl -XPOST http://localhost:8080/realms/skillprofil/protocol/openid-connect/token -k -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=hrm&password=Eisenbart&grant_type=password&client_id=skillprofil-client' | jq -r '.access_token')" -d '{"name": "Kragin", "surname": "Kupferhelm"}'
