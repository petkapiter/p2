for i in range(10):
    print(f'interface FastEthernet0/{i}')

vlans = [10, 20, 30, 40, 50, 60, 70,]
for vlan in vlans:
    print(f'vlan {vlan}')
    print(f' name VLAN_{vlan}')