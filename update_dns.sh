zone_identifier="xxxxxx"
auth_email="xxxxxx@xxxxxx.com"
auth_key="xxxxxx"
record_identifier="xxxxxx"
record_name="xxxxxx.com"
content="xx.xx.xx.xx"
type="A"
proxied="true"
curl -s -X PATCH  "https://api.cloudflare.com/client/v4/zones/$zone_identifier/dns_records/$record_identifier" \
-H "X-Auth-Email: $auth_email" \
-H "X-Auth-Key: $auth_key" \
-H "Content-Type: application/json" \
--data "{\"id\":\"$zone_identifier\",\"type\":\"$type\",\"name\":\"$record_name\",\"content\":\"$content\",\"ttl\":1,\"proxied\":$proxied}"