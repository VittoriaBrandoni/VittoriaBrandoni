# 📡 Attivare la Modalità Monitor in Parrot OS

Guida testata con adattatore USB 802.11n SL-1504N (chipset RTL8191S) su macchina virtuale UTM con Parrot OS.

---

## 🔧 Passaggi

### 1. Verifica interfacce Wi-Fi disponibili (Strumenti utili: airmon-ng, airodump-ng, aircrack-ng, tcpdump)

```bash
iwconfig
sudo ifconfig wlan1 down
sudo ifconfig wlan1 up
iwconfig
