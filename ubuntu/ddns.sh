#vi cf-ddns.sh
# chmod +x /etc/scripts/df-ddns.sh
# */5 * * * * /bin/bash /etc/scripts/cf-ddns.sh >> /var/log/cf-ddns.log 2>&1

####
#!/bin/bash

ZONE_ID="33b0e0a5c550ad768189608a60a43082"
DOMAIN="durgasri.in"
API_TOKEN=""

HOST=$(hostname -s)
RECORD_NAME="$HOST.$DOMAIN"

# Hostname → Record Mapping
case "$HOST" in
    n1)
        RECORD_ID="df45d3e5f6e87ac2fd545f9d74261a59"
        ;;
    n2)
        RECORD_ID="b8c29cbca2ffc09093a74d4baa3ccdeb"
        ;;
    *)
        echo "Unknown hostname: $HOST"
        exit 1
        ;;
esac

DNS_IP=$(dig +short $RECORD_NAME | head -n1)
LOCAL_IP=$(ip route get 1 | awk '{print $7;exit}')

echo "Node        : $HOST"
echo "DNS Record  : $RECORD_NAME"
echo "DNS IP      : $DNS_IP"
echo "LOCAL IP    : $LOCAL_IP"

if [ "$DNS_IP" != "$LOCAL_IP" ]; then
    echo "Updating Cloudflare..."

    RESPONSE=$(curl -s -X PUT \
    "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records/$RECORD_ID" \
    -H "Authorization: Bearer $API_TOKEN" \
    -H "Content-Type: application/json" \
    --data "{\"type\":\"A\",\"name\":\"$RECORD_NAME\",\"content\":\"$LOCAL_IP\",\"ttl\":60,\"proxied\":false}")

    echo "$RESPONSE"
else
    echo "No update needed"
fi