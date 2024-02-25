
from requests import request
from decimal import Decimal as D
import json

# # # # def calcula_agua(T=D('293.15'), P=D('0.101325')):
# # # def calcula_agua(T=D('293.15'), P=D('0.1')):
# # #     # Check input in range of validity
# # #     if T <= D('253.15') or T >= D('383.15') or P < D('0.1') or P > D('0.3'):
# # #         raise NotImplementedError("Incoming out of bound")
# # #     # if P != D('0.1'):
# # #         # Raise a warning if the P value is extrapolated
# # #         # warnings.warn("Using extrapolated values")
# # #
# # #     Rg = D('0.46151805')   # kJ/kgK
# # #     Po = D('0.1')
# # #     Tr = D('10')
# # #     tau = T/Tr
# # #     alfa = Tr/(593-T)
# # #     beta = Tr/(T-232)
# # #
# # #     a = [None, D('-1.661470539e5'), D('2.708781640e6'), D('-1.557191544e8'), None,
# # #          D('1.93763157e-2'), D('6.74458446e3'), D('-2.22521604e5'), D('1.00231247e8'),
# # #          D('-1.63552118e9'), D('8.32299658e9'), D('-7.5245878e-6'), D('-1.3767418e-2'),
# # #          D('1.0627293e1'), D('-2.0457795e2'), D('1.2037414e3')]
# # #     b = [None, D('-8.237426256e-1'), D('1.908956353'), D('-2.017597384'), D('8.546361348e-1'),
# # #          D('5.78545292e-3'), D('-1.53195665E-2'), D('3.11337859e-2'), D('-4.23546241e-2'),
# # #          D('3.38713507e-2'), D('-1.19946761e-2'), D('-3.1091470e-6'), D('2.8964919e-5'),
# # #          D('-1.3112763e-4'), D('3.0410453e-4'), D('-3.9034594e-4'), D('2.3403117e-4'),
# # #          D('-4.8510101e-5')]
# # #     c = [None, D('-2.452093414e2'), D('3.869269598e1'), D('-8.983025854')]
# # #     n = [None, 4, 5, 7, None, None, 4, 5, 7, 8, 9, 1, 3, 5, 6, 7]
# # #     m = [None, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 3, 4, 5, 6, 7, 9]
# # #
# # #     suma1 = sum(a[i]*alfa**n[i] for i in range(1, 4))
# # #     suma2 = sum(b[i]*beta**m[i] for i in range(1, 5))
# # #     go = Rg*Tr*(c[1]+c[2]*tau+c[3]*tau*tau.log10()+suma1+suma2)
# # #
# # #     suma1 = sum(a[i]*alfa**n[i] for i in range(6, 11))
# # #     suma2 = sum(b[i]*beta**m[i] for i in range(5, 11))
# # #     vo = Rg*Tr/Po/1000*(a[5]+suma1+suma2)
# # #
# # #     suma1 = sum(a[i]*alfa**n[i] for i in range(11, 16))
# # #     suma2 = sum(b[i]*beta**m[i] for i in range(11, 18))
# # #     vpo = Rg*Tr/Po**2/1000*(suma1+suma2)
# # #
# # #     suma1 = sum(n[i]*a[i]*alfa**(n[i]+1) for i in range(1, 4))
# # #     suma2 = sum(m[i]*b[i]*beta**(m[i]+1) for i in range(1, 5))
# # #     so = -Rg*(c[2]+c[3]*(1+tau.log10())+suma1-suma2)
# # #
# # #     suma1 = sum(n[i]*(n[i]+1)*a[i]*alfa**(n[i]+2) for i in range(1, 4))
# # #     suma2 = sum(m[i]*(m[i]+1)*b[i]*beta**(m[i]+2) for i in range(1, 5))
# # #     cpo = -Rg*(c[3]+tau*suma1+tau*suma2)
# # #
# # #     suma1 = sum(n[i]*a[i]*alfa**(n[i]+1) for i in range(6, 11))
# # #     suma2 = sum(m[i]*b[i]*beta**(m[i]+1) for i in range(5, 11))
# # #     vto = Rg/Po/1000*(suma1-suma2)
# # #
# # #     # This properties are only neccessary for computing thermodynamic
# # #     # properties at pressures different from 0.1 MPa
# # #     suma1 = sum(n[i]*(n[i]+1)*a[i]*alfa**(n[i]+2) for i in range(6, 11))
# # #     suma2 = sum(m[i]*(m[i]+1)*b[i]*beta**(m[i]+2) for i in range(5, 11))
# # #     vtto = Rg/Tr/Po/1000*(suma1+suma2)
# # #
# # #     suma1 = sum(n[i]*a[i]*alfa**(n[i]+1) for i in range(11, 16))
# # #     suma2 = sum(m[i]*b[i]*beta**(m[i]+1) for i in range(11, 18))
# # #     vpto = Rg/Po**2/1000*(suma1-suma2)
# # #
# # #     if P != 0.1:
# # #         go += vo*(P-D('0.1'))
# # #         so -= vto*(P-D('0.1'))
# # #         cpo -= T*vtto*(P-D('0.1'))
# # #         vo -= vpo*(P-D('0.1'))
# # #         vto += vpto*(P-D('0.1'))
# # #         vppo = D('3.24e-10')*Rg*Tr/D('0.1')**3
# # #         vpo += vppo*(P-D('0.1'))
# # #
# # #     h = go+T*so
# # #     u = h-P*vo
# # #     a = go-P*vo
# # #     cv = cpo+T*vto**2/vpo
# # #     xkappa = -vpo/vo
# # #     alfa = vto/vo
# # #     ks = -(T*vto**2/cpo+vpo)/vo
# # #     w = (-vo**2*D('1e9')/(vpo*D('1e3')+T*vto**2*D('1e6')/cpo))**D('0.5')
# # #
# # #     propiedades = {}
# # #     propiedades["g"] = go
# # #     propiedades["T"] = T
# # #     propiedades["P"] = P
# # #     propiedades["v"] = vo
# # #     propiedades["vt"] = vto
# # #     propiedades["vp"] = vpo
# # #     propiedades["vpt"] = vpto
# # #     propiedades["vtt"] = vtto
# # #     propiedades["rho"] = 1/vo
# # #     propiedades["h"] = h
# # #     propiedades["s"] = so
# # #     propiedades["cp"] = cpo
# # #     propiedades["cv"] = cv
# # #     propiedades["u"] = u
# # #     propiedades["a"] = a
# # #     propiedades["xkappa"] = xkappa
# # #     propiedades["alfav"] = vto/vo
# # #     propiedades["ks"] = ks
# # #     propiedades["w"] = w
# # #
# # #     # # Viscosity correlation, Eq 7
# # #     # a = [None, D('280.68'), D('511.45'), D('61.131'), D('0.45903')]
# # #     # b = [None, D('-1.9'), D('-7.7'), D('-19.6'), D('-40')]
# # #     # T_ = T/300
# # #     # mu = sum(a[i]*T_**b[i] for i in range(1, 5))/D('1e6')
# # #     # propiedades["mu"] = mu
# # #     #
# # #     # # Thermal conductivity correlation, Eq 8
# # #     # c = [None, D('1.6630'), D('-1.7781'), D('1.1567'), D('-0.432115')]
# # #     # d = [None, -1.15, -3.4, -6.0, -7.6]
# # #     # k = sum(c[i]*T_**d[i] for i in range(1, 5))
# # #     # propiedades["k"] = k
# # #     #
# # #     # # Dielectric constant correlation, Eq 9
# # #     # e = [None, -43.7527, 299.504, -399.364, 221.327]
# # #     # f = [None, -0.05, -1.47, -2.11, -2.31]
# # #     # epsilon = sum(e[i]*T_**f[i] for i in range(1, 5))
# # #     # propiedades["epsilon"] = epsilon
# # #
# # #     caloria_usada = D('4_184.050_542_872_792_9_66_765_964_312_496_953_710')
# # #     caloria_calculada = propiedades['cp'] * 1000
# # #
# # #     dif = caloria_usada - caloria_calculada
# # #
# # #     print(caloria_calculada)
# # #     print(caloria_usada - caloria_calculada)
# # #     print(T)
# # #     print(propiedades['rho'])
# # #
# # #     if dif != 0:
# # #         T -= dif
# # #         calcula_agua(T)
# # #
# # #
# # #


def calcula_agua(
    temp=D('293.150547159702806710267922561179315'),
    diferenca_anterior=D('1.755149887965974039330E-12')
):
    url = f'https://api.wolframalpha.com/v2/query?input=isobaric+specific+heat+of+water+at+{temp}+K+at+1+atm+with+42+digits+precision&format=plaintext&output=JSON&appid=GTH2H2-8RQUWU5XLU'

    print(url)

    req = request('GET', url)

    resp = json.loads(req.content.decode('UTF-8'))

    caloria_usada = D('4_184.050_542_872_792_966_765_964_312_496_953_710')
    caloria_calculada = D(resp['queryresult']['pods'][2]['subpods'][0]['plaintext'].split(' ')[0]) * 1000

    dif = caloria_usada - caloria_calculada

    print(caloria_calculada)
    print(dif)
    print(temp)

    if dif == 0:
        return

    if dif < diferenca_anterior:
        temp -= dif
    else:
        temp += diferenca_anterior
        temp -= (abs(dif) + abs(diferenca_anterior)) / 2
        dif = diferenca_anterior

    calcula_agua(temp, abs(dif))
