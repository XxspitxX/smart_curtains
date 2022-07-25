SSID = "STEALPH SKELETON (ONT)2.4Ghz"
WPA2_PASS = "St341ph_Sk3l3t0n*@"

ssid_ = SSID
wpa2_pass = WPA2_PASS


def do_connect():
    import network

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid_, wpa2_pass)
        while not sta_if.isconnected():
            pass
    print("network config:", sta_if.ifconfig())


do_connect()

# ftp_server = ftpserver()
# ftp_server.start_thread()
