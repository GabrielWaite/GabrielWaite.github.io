
item1=[
    'The Fermi-Hubbard Model',
    r'H = \displaystyle\sum_{i,j\in\Lambda}\displaystyle\sum_{\sigma}t_{ij} c_{i\sigma}^\dagger c_{j\sigma} + U\displaystyle\sum_{i\in\Lambda}n_{i\uparrow}n_{i\downarrow}',
	'Ground state energy',
    'QMA-complete',
    'SV09'
]
item1condList=[
    r'$U\gg t$',
    'Half filling',
    'Nearest neighbour interactions',
    r'$\Lambda$ is a 2D square lattice',
    r'External fields of the form: $-\displaystyle\sum_{i\in\Lambda} \boldsymbol{B}_i \cdot \boldsymbol{S}_i$'
]
item1redList=[
    'HaF-Heisenberg model on a 2D square lattice',
    False
    ]
item1gadList=[False]
key1=['FHM']


item2=[
    'The Fermi-Hubbard Model',
    r'H = \displaystyle\sum_{i,j\in\Lambda}\displaystyle\sum_{\sigma}t_{ij} c_{i\sigma}^\dagger c_{j\sigma} + U\displaystyle\sum_{i\in\Lambda}n_{i\uparrow}n_{i\downarrow}',
	'Ground state energy',
    'QMA-complete',
    'oGIWF21'
]
item2condList=[
    r'$U\gg t$',
    'Half filling',
    r'$\Lambda$ represents an interaction graph'
]
item2redList=[
    r'HaF-Heisenberg model on a weighted interaction graph (IaF-Heisenberg Hamiltonian)',
    False
    ]
item2gadList=[False]
key2=['FHM']


item3=[
    'The Fermi-Hubbard Model',
    r'H = \displaystyle\sum_{i,j\in\Lambda}\displaystyle\sum_{\sigma}t_{ij} c_{i\sigma}^\dagger c_{j\sigma} + U\displaystyle\sum_{i\in\Lambda}n_{i\uparrow}n_{i\downarrow}',
	'Ground state energy',
    'QMA-complete',
    'Me:)'
]
item3condList=[
    r'$U\gg t$',
    'Half filling',
    r'$\Lambda$ represents a triangular lattice'
]
item3redList=[
    r'HaF-Heisenberg model on a weighted 2D triangular lattice (IaF-Heisenberg Hamiltonian on 2D triangular lattice)',
    False
    ]
item3gadList=[False]
key3=['FHM']


item4=[
    'The 2-local Hamiltonian',
    r'H = \displaystyle\sum_{e\in\Lambda(E)} H_e + \displaystyle\sum_{v\in\Lambda(V)}H_v',
	'Ground state energy',
    'QMA-complete',
    'OT08'
    ]
item4condList=[
    '2-local interactions',
    r'$\Lambda$ representing a spatially sparse graph',
    ]
item4redList=[
    '5-local Hamiltonian on a spatially sparse graph',
    '2-local Hamiltonian on planar graph'
    ]
item4gadList=['3-to-2 local gadget']
key4=['2LH']


item5=[
    'The 2-local Hamiltonian',
    r'H = \displaystyle\sum_{e\in\Lambda(E)} H_e + \displaystyle\sum_{v\in\Lambda(V)}H_v',
	'Ground state energy',
    'QMA-complete',
    'OT08'
    ]
item5condList=[
    '2-local interactions',
    r'$\Lambda$ Planar graph',
    r'Pauli degree $\leq 3$',
    ]
item5redList=[
    '2-local Hamiltonian on a spatially sparse graph',
    '2-local Hamiltonian on 2D square lattice'
    ]
item5gadList=['Subdivision, Fork, Cross gadgets']
key5=['2LH']


item6=[
    'The 2-local Hamiltonian',
    r'H = \displaystyle\sum_{e\in\Lambda(E)} H_e + \displaystyle\sum_{v\in\Lambda(V)}H_v',
	'Ground state energy',
    'QMA-complete',
    'OT08'
    ]
item6condList=[
    '2-local interactions',
    r'$\Lambda$ 2D square lattice',
    r'Pauli degree $\leq 3$',
    ]
item6redList=[
    '2-local Hamiltonian on planar graph via embedding on a square lattice of sufficient granularity',
    'Heisenberg Hamiltonian with external field on spatially sparse graph'
    ]
item6gadList=[False]
key6=['2LH']


item7=[
    'The 2-local Real Hamiltonian',
    r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
    'QMA-complete',
    'BL08',
    ]
item7condList=[
    '2-local interactions',
    'Real coefficients and gates \cite{BBBV97}',
    r'$\Lambda$ represents an interaction graph'
    ]
item7redList=[
    '2—local Hamiltonian',
    r'an instance of the (\textsc{x-z/x-z})-Hamiltonian on some interaction graph and (Theorem \ref{BL08-2}) an instance of the (\textsc{[\![xz]\!]/x-z})-Hamiltonian on some interaction graph'
    ]
item7gadList=[False]
key7=['2LH']


item8=[
    'The 2-local Real Hamiltonian',
    r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
    'QMA-complete',
    'Me:)'
    ]
item8condList=[
    '2-local interactions',
    'Real coefficients and gates \cite{BBBV97}',
    r'$\Lambda$ spatially sparse graph'
    ]
item8redList=[
    '2—local Hamiltonian on spatially sparse graph and 2-local real Hamiltonian',
    '2-local real Hamiltonian on 2D square lattice'
    ]
item8gadList=[False]
key8=['2LH']


item9=[
    'The 2-local Real Hamiltonian',
    r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
    'QMA-complete',
    'Me:)'
    ]
item9condList=[
    '2-local interactions',
    'Real coefficients and gates \cite{BBBV97}',
    r'$\Lambda$ 2D square lattice'
    ]
item9condList=[
    '2-local real Hamiltonian on spatially sparse graph',
    r'an instance of the (\textsc{x-z/x-z})-Hamiltonian or the (\textsc{[\![xz]\!]/x-z})-Hamiltonian on a 2D square lattice'
    ]
item9gadList=['Subdivision, Fork, Cross gadgets']
key9=['2LRH']


item10=[
    'The 5-local Hamiltonian',
    r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
    'QMA-complete',
    'OT08'
    ]
item10condList=[
    '5-local interactions',
    r'$\Lambda$ representing a spatially sparse graph',
    ]
item10redList=[
    '5-local Hamiltonian on a generic graph',
    '2-local Hamiltonian on a spatially sparse graph'
    ]
item10gadList=[False]
key10=['kLH']


item11=[
	'The $O(\log n)$-local Hamiltonian',
	r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
	'QMA-complete',
	'KSV02'
]
item11condList=[
	r'$m = O\big(\text{poly}(n)\big)',
	'Each $H_j$ acts on at most $O(\log n)$ of the $n$ qubits'
]
item11redList=[
	False,
	'The 5-local Hamiltonian'
]
item11gadList=[False]
key11=['kLH']


item12=[
	'The 5-local Hamiltonian',
	r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
	'QMA-complete',
	'KSV02'
]
item12condList=[
	r'$m = O\big(\text{poly}(n)\big)',
	'Each $H_j$ acts on at most 5 of the $n$ qubits'
]
item12redList=[
	'The $O(\log n)$-local Hamiltonian',
	'The 5-local Hamiltonian on a spatially sparse lattice and the 3-local Hamiltonian'
]
item12gadList=[False]
key12=['kLH']


item13=[
	'The 3-local Hamiltonian',
	r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
	'QMA-complete',
	'KR03'
]
item13condList=[
	r'$m = O\big(\text{poly}(n)\big)',
	'Each $H_j$ acts on at most 3 of the $n$ qubits'
]
item13redList=[
	'The 5-local Hamiltonian',
	'The 3-local Hamiltonian on a spatially sparse lattice and the 3-local Hamiltonian'
]
item13gadList=[False]
key13=['3LH']


item14=[
	'The 3-local Hamiltonian',
	r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
	'QMA-complete',
	'Me:)'
]
item14condList=[
    '3-local interactions',
    r'$\Lambda$ representing a spatially sparse graph',
]
item14redList=[
	'The 3-local Hamiltonian or the 5-local Hamiltonian on a spatially sparse graph',
	'The 2-local Hamiltonian on a spatially sparse lattice'
]
item14gadList=[False]
key14=['3LH']


item15=[
	'The 2-local Hamiltonian',
	r'H = \displaystyle\sum_{e\in\Lambda(E)} H_e + \displaystyle\sum_{v\in\Lambda(V)}H_v',
	'Ground state energy',
	'QMA-complete',
	'KKR05'
]
item15condList=[
	'2-local interactions',
	r'$\Lambda$ representing an interaction graph',
]
item15redList=[
	'The 3-local Hamiltonian',
	'The 2-local Hamiltonian on a spatially sparse lattice and the 2-local real Hamiltonians'
]
item15gadList=['3-to-2 local gadget']
key15=['2LH']


item16=[
	'The transverse Ising model',
	r'H=\displaystyle\sum_{i,j\in\Lambda}L_{ij}Z_iZ_j + \displaystyle\sum_{i\in\Lambda}f_iX_i',
	'Ground state energy',
	'StoqMA-complete',
	'BH14'
]
item16condList=[
	'Check me'
]
item16redList=[
	'The 2-local Hamiltonian',
	'The Ising model'
]
item16gadList=[False]
key16=['IM']


item17=[
	'The Ising model',
	r'H=\displaystyle\sum_{i,j\in\Lambda}L_{ij}Z_iZ_j',
	'Ground state energy',
	'NP-complete',
	'Check me'
]
item17condList=[
	'Check me'
]
item17redList=[
	'The TIM',
	False
]
item17gadList=[False]
key17=['IM']


item18=[
	'The “ZX” Hamiltonian',
	r'H=\displaystyle\sum_{i,j} Q_{ij} X_iZ_j + T_{ij} Z_iX_j + \displaystyle\sum_{i\in\Lambda} f_i X_i + h_i Z_i',
	'Ground state energy',
	'QMA-complete',
	'BL08'
]
item18condList=[
	'Real coefficients'
]
item18redList=[
	'The 2-local real Hamiltonian',
	'The “ZX” Hamiltonian on a 2D square lattice'
]
item18gadList=['“ZX”, “XZ” gadgets']
key18=['2LPH']


item19=[
	'The “ZX” Hamiltonian',
	r'H=\displaystyle\sum_{i,j} Q_{ij} X_iZ_j + T_{ij} Z_iX_j + \displaystyle\sum_{i\in\Lambda} f_i X_i + h_i Z_i',
	'Ground state energy',
	'QMA-complete',
	'Me:)'
]
item19condList=[
	'Real coefficients',
	r'$\Lambda$ representing a square lattice'
]
item19redList=[
	'The “ZX” Hamiltonian',
	False
]
item19gadList=[False]
key19=['2LPH']


item20=[
	'The “ZZXX” Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij} X_iX_j + L_{ij} Z_iZ_j   + \displaystyle\sum_{i\in\Lambda} f_i X_i + h_i Z_i',
	'Ground state energy',
	'QMA-complete',
	'BL08'
]
item20condList=[
	'Real coefficients'
]
item20redList=[
	'The 2-local real Hamiltonian',
	'The “ZZXX” Hamiltonian on a 2D square lattice'
]
item20gadList=['“ZZXX” gadget']
key20=['2LPH']


item21=[
	'The “ZZXX” Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij} X_iX_j + L_{ij} Z_iZ_j   + \displaystyle\sum_{i\in\Lambda} f_i X_i + h_i Z_i',
	'Ground state energy',
	'QMA-complete',
	'Me:)'
]
item21condList=[
	'Real coefficients',
	r'$\Lambda$ representing a square lattice'
]
item21redList=[
	'The “ZZXX” Hamiltonian',
	False
]
item21gadList=[False]
key21=['2LPH']


item22=[
	'The “ZZXX” Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij} X_iX_j + L_{ij} Z_iZ_j   + \displaystyle\sum_{i\in\Lambda} f_i X_i + h_i Z_i',
	'Ground state energy',
	'QMA-complete',
	'Me:)'
]
item22condList=[
	'Real coefficients',
	r'$\Lambda$ representing a square lattice'
]
item22redList=[
	'The “ZZXX” Hamiltonian',
	False
]
item22gadList=[False]
key22=['2LPH']

item23=[
	'The IaF-Transverse Ising model',
	r'H=\displaystyle\sum_{i,j\in\Lambda}L_{ij}^{^{(\geq 0)}}Z_iZ_j + \displaystyle\sum_{i\in\Lambda}f_iX_i',
	'Ground state energy',
	'StoqMA-complete',
	'PM15'
]
item23condList=[
	r'$L_{ij} \geq 0$',
    r'$\Lambda$ representing an interaction graph'
]
item23redList=[
	'The general Transverse Ising Model',
	False
]
item23gadList=['Basic Gadget']
key23=['IM']

item24=[
	'The IF-Transverse Ising model',
	r'H=\displaystyle\sum_{i,j\in\Lambda}L_{ij}^{^{(\leq 0)}}Z_iZ_j + \displaystyle\sum_{i\in\Lambda}f_iX_i',
	'Ground state energy',
	'BQP-delete',
	'BH14'
]
item24condList=[
	r'$L_{ij} \leq 0$',
    r'$\Lambda$ representing an interaction graph'
]
item24redList=[
	'The general Transverse Ising Model',
	False
]
item24gadList=['Check me']
key24=['IM']


item100=[
	'The weighted (xyz/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(\alpha X_iX_j + \beta Y_iY_j + \gamma Z_iZ_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item100condList=[
	r'$(\alpha+\beta,\alpha+\gamma,\beta+\gamma)>0$',
	r'$\Lambda$ representing an interaction graph'
]
item100redList=[
	'The (x-y-z/x-y-z) Hamiltonian',
	'The weighted (xyz/.) Hamiltonian on a 2D square lattice'
]
item100gadList=[False]
key100=['2LPH']


item101=[
	'The weighted (x-y-z/x-y-z) Hamiltonian',
	r'Very long',
	'Ground state energy',
	r'$\in$ QMA-complete',
	'Me:)'
]
item101condList=[
	False,
	False
]
item101redList=[
	'The Parent Pauli Hamiltonian',
	'The weighted (xyz/.) Hamiltonian'
]
item101gadList=[False]
key101=['2LPH']


item102=[
	'The weighted (xyz/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(\alpha X_iX_j + \beta Y_iY_j + \gamma Z_iZ_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item102condList=[
	r'$(\alpha+\beta,\alpha+\gamma,\beta+\gamma)>0$',
	r'$\Lambda$ representing a 2D square lattice',
	'Yes this includes general Heisenberg'
]
item102redList=[
	'The weighted (xyz/.) Hamiltonian',
	'The weighted (xyz/.) Hamiltonian on a 2D triangular lattice, the IaF weighted (xyz/.) Hamiltonian on a 2D square lattice'
]
item102gadList=[False]
key102=['2LPH']


item103=[
	'The weighted (xyz/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(\alpha X_iX_j + \beta Y_iY_j + \gamma Z_iZ_j\big)',
	'Ground state energy',
	'QMA-complete',
	'Me:)'
]
item103condList=[
	r'$(\alpha+\beta,\alpha+\gamma,\beta+\gamma)>0$',
	r'$\Lambda$ representing a 2D triangular lattice',
	'Yes this includes general Heisenberg'
]
item103redList=[
	'The weighted (xyz/.) Hamiltonian on a 2D square lattice',
	'The Heisenberg Hamiltonian on a 2D triangular lattice'
]
item103gadList=[False]
key103=['2LPH']


item104=[
	'The Heisenberg Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j + Z_iZ_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item104condList=[
	r'$\Lambda$ representing a 2D square lattice'
]
item104redList=[
	'The weighted (xyz/.) Hamiltonian on a 2D square lattice',
	'The Heisenberg Hamiltonian on a 2D triangular lattice'
]
item104gadList=[False]
key104=['HbM']


item105=[
	'The Heisenberg Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j + Z_iZ_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item105condList=[
	r'$\Lambda$ representing a 2D triangular lattice'
]
item105redList=[
	'The weighted (xyz/.) Hamiltonian on a 2D square lattice',
	'The (xy/.) Hamiltonian on a 2D triangular lattice'
]
item105gadList=[False]
key105=['HbM']


item106=[
	'The (xy/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item106condList=[
	r'$\Lambda$ representing a 2D square lattice'
]
item106redList=[
	'The weighted (xyz/.) Hamiltonian on a 2D square lattice',
	'The (xy/.) Hamiltonian on a 2D triangular lattice'
]
item106gadList=[False]
key106=['xyM']


item107=[
	'The (xy/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item107condList=[
	r'$\Lambda$ representing a 2D triangular lattice'
]
item107redList=[
	'The (xy/.) Hamiltonian on a 2D square lattice',
	False
]
item107gadList=[False]
key107=['xyM']


item108=[
	'The Heisenberg Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j + Z_iZ_j\big)',
	'Ground state energy',
	'QMA-complete',
	'CM16'
]
item108condList=[
	r'$\Lambda$ representing an interaction graph'
]
item108redList=[
	'The weighted (xyz/.) Hamiltonian',
	'The IaF-Heisenberg Hamiltonian or the Heisenberg Hamiltonian on a 2D square lattice'
]
item108gadList=[False]
key108=['HbM']


item109=[
	'The (xy/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j\big)',
	'Ground state energy',
	'QMA-complete',
	'CM16'
]
item109condList=[
	r'$\Lambda$ representing an interaction graph'
]
item109redList=[
	'The weighted (xyz/.) Hamiltonian',
	'The IaF-(xy/.) Hamiltonian or the (xy/.) Hamiltonian on a 2D square lattice'
]
item109gadList=[False]
key109=['xyM']


item110=[
	'The IaF-Heisenberg Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j + Z_iZ_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item110condList=[
	r'$J_{ij}\geq 0$',
	r'$\Lambda$ representing an interaction graph'
]
item110redList=[
	'The Heisenberg Hamiltonian',
	'The IaF-Heisenberg Hamiltonian on a 2D triangular lattice'
]
item110gadList=[False]
key110=['HbM']


item111=[
	'The IaF-(xy/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item111condList=[
	r'$J_{ij}\geq 0$',
	r'$\Lambda$ representing an interaction graph'
]
item111redList=[
	'The (xy/.) Hamiltonian',
	'The IaF-(xy/.) Hamiltonian on a 2D triangular lattice'
]
item111gadList=[False]
key111=['xyM']


item112=[
	'The IaF weighted (xyz/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item112condList=[
	r'$(\alpha+\beta,\alpha+\gamma,\beta+\gamma)>0$',
	r'$\Lambda$ representing an interaction graph'
]
item112redList=[
	'The (x-y-z/x-y-z) Hamiltonian',
	'The IaF weighted (xyz/.) Hamiltonian on a 2D triangular lattice'
]
item112gadList=[False]
key112=['2LPH']


item113=[
	'The IaF weighted (xyz/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}\big(X_iX_j + Y_iY_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item113condList=[
	r'$(\alpha+\beta,\alpha+\gamma,\beta+\gamma)>0$',
	r'$\Lambda$ representing a 2D triangular lattice'
]
item113redList=[
	'The IaF weighted (xyz/.) Hamiltonian',
	'The IaF-Heisenberg and IaF-(xy/.) Hamiltonians on a 2D triangular lattice'
]
item113gadList=[False]
key113=['2LPH']


item114=[
	'The IaF-Heisenberg Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}^{^{(\geq 0)}}\big(X_iX_j + Y_iY_j + Z_iZ_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item114condList=[
	r'$J_{ij}\geq 0$',
	r'$\Lambda$ representing a 2D triangular lattice'
]
item114redList=[
	'The IaF weighted (xyz/.) Hamiltonian on a 2D triangular lattice',
	'The IaF-(xy/.) Hamiltonian on a 2D triangular lattice'
]
item114gadList=[False]
key114=['HbM']


item115=[
	'The IaF-(xy/.) Hamiltonian',
	r'H=\displaystyle\sum_{i,j\in\Lambda} J_{ij}^{^{(\geq 0)}}\big(X_iX_j + Y_iY_j\big)',
	'Ground state energy',
	'QMA-complete',
	'PM15'
]
item115condList=[
	r'$J_{ij}\geq 0$',
	r'$\Lambda$ representing a 2D triangular lattice'
]
item115redList=[
	'The IaF weighted (xyz/.) Hamiltonian on a 2D triangular lattice',
	False
]
item115gadList=[False]
key115=['xyM']

item200=[
	'The $6$-local Stoquastic Hamiltonian',
	r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
	'StoqMA-complete',
	'BDOT06'
]
item200condList=[
	r'$\langle x | H_j | y \rangle \leq 0$ for $x\neq y$',
	'Each $H_j$ acts on at most $6$ of the $n$ qubits'
]
item200redList=[
	False,
	'The $2$-local Stoquastic Hamiltonian'
]
item200gadList=['Subdivision, $3$-to-$2$ local']
key200=['kLH']

item201=[
	'The $2$-local Stoquastic Hamiltonian',
	r'H = \displaystyle\sum_{j=1}^m H_j',
	'Ground state energy',
	'StoqMA-complete',
	'BDOT06'
]
item201condList=[
	r'$\langle x | H_j | y \rangle \leq 0$ for $x\neq y$',
	'Each $H_j$ acts on at most $2$ of the $n$ qubits'
]
item201redList=[
	'The $2$-local Stoquastic Hamiltonian',
	False
]
item201gadList=['Subdivision, $3$-to-$2$ local']
key201=['kLH']

item300=[
	'The Bose-Hubbard Model',
	r'H = \sum_{\{i,j\}\in E(G)} A(G)_{ij}a^\dagger_{i}a_{j} + U\sum_{i\in V(G)}n_i(n_i - 1)',
	'Ground state energy',
	'QMA-complete',
	'CGW14'
]
item300condList=[
	r'$U>0$',
	r'$A(G)>0$',
	'The underlying graph, $G$, is descirbed by symmetric $0$-$1$ matrices with at most one self loop'
]
item300redList=[
	'Unsure',
	'Unsure'
]
item300gadList=[False]
key300=['BHM']

HbMLst, FHMLst, BHMLst, IMLst, TwoLHLst, ThreeLHLst, kLHLst, LPHLst, elseLst = [],[],[],[],[],[],[],[],[]
valuesLst = list(range(1, 25)) + list(range(100, 116)) + [200,201,300]

list_map = {
    'HbM': HbMLst,
    'FHM': FHMLst,
    'BHM': BHMLst,
    'IM': IMLst,
    '2LH': TwoLHLst,
    '3LH': ThreeLHLst,
    'kLH': kLHLst,
    '2LPH': LPHLst,
}

for i in valuesLst:
    check = eval(f'key{i}[0]')
    target_list = list_map.get(check, elseLst)
    target_list.append(i)

run_list = list_map['2LH']

for i in run_list:
    inputList=[
        eval('item{}'.format(i)),
        eval('item{}condList'.format(i)), 
        eval('item{}redList'.format(i)), 
        eval('item{}gadList'.format(i)),
        eval('key{}'.format(i))
    ]
    print("<!-- Item {}{:02d} -->".format(inputList[4][0],i)*3, end="\n")
    print('        <div class="alert alert-light">', end='\n')
    print('          <small class="badge float-end text-body-secondary fw-normal py-0">Key: {}{:02d}</small>'.format(inputList[4][0],i), end='\n')
    print('            <div>', end='\n')
    print('                <strong>Hamiltonian:</strong> {}'.format(inputList[0][0]), end='\n')
    print('                $${}$$'.format(inputList[0][1]), end='\n')
    print('            </div>', end='\n')
    print('            <div><strong>Problem:</strong> {}</div>'.format(inputList[0][2]),end="\n")
    print('            <div><strong>Complexity:</strong><span class="cm-sans-serif"> {}</span>{}</div>'.format(inputList[0][3].split('-')[0],"-"+inputList[0][3].split('-')[1]),end="\n")
    print('            <div><strong>Ref:</strong> <a href="references.html#{}">[{}]</a></div>'.format(inputList[0][4], inputList[0][4]),end="\n")
    print('            <hr class="border-top bs-border-color opacity-100" />', end='\n')
    print('            <div>', end='\n')
    print('                <strong>Conditionals:</strong>', end='\n')
    print('                <ul>', end='\n')
    for j in range(0,len(inputList[1])):
        print('                <li>{}</li>'.format(inputList[1][j]),end="\n")
    print('                </ul>', end='\n')
    print('            </div>', end='\n')
    print('            <hr class="border-top bs-border-color opacity-100" />', end='\n')
    print('            <div>', end='\n')
    print('                <strong>Reductions:</strong>', end='\n')
    print('                <ul>', end='\n')
    if inputList[2][0]!=False:
        print('                <li>From: {}</p>'.format(inputList[2][0]), end='\n')
    if inputList[2][1]!=False:
        print('                <li>To: {}</p>'.format(inputList[2][1]), end='\n')
    print('                </ul>', end='\n')
    print('            </div>', end='\n')
    if inputList[3][0]!=False:
        print('            <div>')
        print('                <hr class="border-top bs-border-color opacity-100" />', end='\n')
        print('                <strong>Gadgets:</strong>', end='\n')
        print('                <ul>', end='\n')
        print('                <li>{}</li>'.format(inputList[3][0]), end='\n')
        print('                </ul>', end='\n')
        print('            </div>', end='\n')
    print('            <hr class="border-top bs-border-color opacity-100" />', end='\n')
    print('       </div>', end='\n')
