import xtlsapi
from hiddifypanel.models import *
from .abstract_driver import DriverABS


class XrayApi(DriverABS):
    def get_xray_client(self):
        if hconfig(ConfigEnum.is_parent):
            return
        return xtlsapi.XrayClient('127.0.0.1', 10085)

    def get_enabled_users(self):
        if hconfig(ConfigEnum.is_parent):
            return
        xray_client = self.get_xray_client()
        users = User.query.all()
        t = "xtls"
        protocol = "vless"
        enabled = {}
        for u in users:
            uuid = u.uuid
            try:
                xray_client.add_client(t, f'{uuid}', f'{uuid}@hiddify.com', protocol=protocol, flow='xtls-rprx-vision', alter_id=0, cipher='chacha20_poly1305')
                xray_client.remove_client(t, f'{uuid}@hiddify.com')
                enabled[uuid] = 0
            except xtlsapi.xtlsapi.exceptions.EmailAlreadyExists as e:
                enabled[uuid] = 1
            except Exception as e:
                print(f"error {e}")
                enabled[uuid] = e
        return enabled

    def get_inbound_tags(self):
        if hconfig(ConfigEnum.is_parent):
            return
        try:
            xray_client = self.get_xray_client()
            inbounds = [inb.name.split(">>>")[1] for inb in xray_client.stats_query('inbound')]
            print(f"Success in get inbound tags {inbounds}")
        except Exception as e:
            print(f"error in get inbound tags {e}")
            inbounds = []
        return list(set(inbounds))

    def add_client(self, user):
        if hconfig(ConfigEnum.is_parent):
            return
        uuid = user.uuid
        xray_client = self.get_xray_client()
        tags = self.get_inbound_tags()
        proto_map = {
            'vless': 'vless',
            'realityin': 'vless',
            'xtls': 'vless',
            'quic': 'vless',
            'trojan': 'trojan',
            'vmess': 'vmess',
            'ss': 'shadowsocks',
            'v2ray': 'shadowsocks',
            'kcp': 'vless',
            'dispatcher': 'trojan',
        }

        def proto(t):
            res = '', ''
            for p, protocol in proto_map.items():
                if p in t:
                    res = p, protocol
                    break
            return res
        for t in tags:
            try:
                p, protocol = proto(t)
                if not p:
                    continue
                if (protocol == "vless" and p != "xtls" and p != "realityin") or "realityingrpc" in t:
                    xray_client.add_client(t, f'{uuid}', f'{uuid}@hiddify.com', protocol=protocol, flow='\0',)
                else:
                    xray_client.add_client(t, f'{uuid}', f'{uuid}@hiddify.com', protocol=protocol,
                                           flow='xtls-rprx-vision', alter_id=0, cipher='chacha20_poly1305')
                # print(f"Success add  {uuid} {t}")
            except Exception as e:
                # print(f"error in add  {uuid} {t} {e}")
                pass

    def remove_client(self, user):
        uuid = user.uuid
        xray_client = self.get_xray_client()
        tags = self.get_inbound_tags()

        for t in tags:
            try:
                xray_client.remove_client(t, f'{uuid}@hiddify.com')
                print(f"Success remove  {uuid} {t}")
            except Exception as e:
                print(f"error in remove  {uuid} {t} {e}")
                pass

    def get_all_usage(self, users):
        return {u: self.get_usage_imp(u.uuid) for u in users}

    def get_usage_imp(self, uuid):
        xray_client = self.get_xray_client()
        d = xray_client.get_client_download_traffic(f'{uuid}@hiddify.com', reset=True)
        u = xray_client.get_client_upload_traffic(f'{uuid}@hiddify.com', reset=True)

        res = None
        if d is None:
            res = u
        elif u is None:
            res = d
        else:
            res = d + u
        if res:
            print(f"Xray usage {uuid} d={d} u={u} sum={res}")
        return res
