# python-web-chat
Web App to chat with your friends.

# Application protocol
The client must send a structured bytes that represent a json with the following fields:
```json
{
    "timestamp": 129389120
	"username":"John Doe", 
	"data": [
		{"type": "text", "content": "Lorem Ipsulum Dolum"},
		{"type": "image", "content": "x00"},
		{"type": "audio", "content": "x00"},
		{"type": "binary", "content": "x00"}
	],
}
```
