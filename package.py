import json


class Package(object):
    string = None  # String care caracterizeaza un pachet.

    def __init__(self, ethernet_dst='', ethernet_src='',
                 ip_dst='', ip_src='', ip_ver='', ip_protocol='',
                 tcp_sport='', tcp_dport='',
                 udp_sport='', udp_dport=''):
        """
        Constructor ce initializeaza clasa Package.
        Contine toate elementele componente ale unui pachet, conform cerintei.
        La crearea unui obiect de tip Package, valorile default ale campurilor sunt niste String-uri goale.
        """
        self.Ethernet_dst = ethernet_dst
        self.Ethernet_src = ethernet_src
        self.IP_dst = ip_dst
        self.IP_src = ip_src
        self.IP_version = ip_ver
        self.IP_protocol = ip_protocol
        self.TCP_sport = tcp_sport
        self.TCP_dport = tcp_dport
        self.UDP_sport = udp_sport
        self.UDP_dport = udp_dport

    def format_json(self):
        """
        Creeaza stringul ce caracterizeaza un pachet.
        :return: Stringul formatat ca JSON.
        """
        self.string = {
            'Ethernet': {
                'source': self.Ethernet_src,
                'destination': self.Ethernet_dst},
            'IP': {
                'source': self.IP_src,
                'destination': self.IP_dst,
                'version': self.IP_version,
                'protocol': self.IP_protocol},
            'TCP': {
                'sport': self.TCP_sport,
                'dport': self.TCP_dport
            },
            'UDP': {
                'sport': self.UDP_sport,
                'dport': self.UDP_dport
            }
        }
        return self.string

    def __str__(self):
        """
        Suprascrierea metodei __str__().
        :return: Un obiect de tip JSON cu caracteristicile unui Pachet.
        """
        self.format_json()
        return json.dumps(self.string)

    def get_string(self):
        """
        :return: String-ul caracteristic al fiecarui pachet.
        """
        self.format_json()
        return self.string

    def is_tcp(self):
        """
        Metoda prin care verific daca Pachetul este de tip TCP
        """
        if self.TCP_sport == '' and self.TCP_dport == '':
            return False
        else:
            return True

    def is_udp(self):
        """
        Metoda prin care verific daca Pachestul este de tip UDP.
        """
        if self.UDP_sport == '' and self.UDP_dport == '':
            return False
        else:
            return True
