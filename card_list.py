# Normal List = 39
# Last Card = 5
List = [\
	{'eng_title':"SERMONE", 'han_title':"예배 시간",\
	'description':"자신의 턴, <뱅!> 카드를 사용 금지."},\
	{'eng_title':"ROULETTE RUSSA", 'han_title':"러시안 룰렛",\
	'description':"이 카드가 발동한 순간, 보완관부터 시작해 순서대로 <빗나감!> 카드를 1장씩 버림. 만약 카드를 버리지 못할 경우, 그 플레이어는 생명령 -2"},\
	{'eng_title':"DEAD MAN", 'han_title':"돌아온 망자",\
	'description':"게임에서 처음 제거된 플레이어는 생명력 2와 카드 2장을 가진 상태로 부활."},\
	{'eng_title':"AGGUATO", 'han_title':"습격",\
	'description':"모든 플레이어 간의 거리는 1이 됨."},\
	{'eng_title':"BENEDIZIONE", 'han_title':"축복",\
	'description':"모든 카드를 하트로 취급함."},\
	{'eng_title':"NOUVA IDENTITA", 'han_title':"새로운 자아",\
	'description':"각 플레이어는 다른 플레이어의 캐릭터 카드를 확인한 후, 생명력 제한에 위배되지 않을 경우, 캐릭터를 교환할 수 있음. 교환할 경우, 생명력 2로 시작함."},\
	{'eng_title':"CITTA' FANTASMA", 'han_title':"유령 마을",\
	'description':"죽은 플레이어는 각자 원래 차례에 3장을 드로우한 상태에서 부활하며, 사망하지 않음. 자신의 턴이 종료하면 유령은 게임에서 다시 퇴장."},\
	{'eng_title':"CORSA ALL'ORO", 'han_title':"골드러시",\
	'description':"이번 라운드만, 카드 효과를 포함한 모든 차례가 반대 방향으로 돌아감."},\
	{'eng_title':"DOROTHY RAGE", 'han_title':"도로시 레이지",\
	'description':"자신의 턴, 다른 플레이어 한 명이 특정 카드 1장을 사용하라 강요할 수 있음.(없으면 무효)"},\
	{'eng_title':"BAVAGLIO", 'han_title':"재갈",\
	'description':"모든 플레이어는 말을 할 수 없음.(어길 경우 생명력 -1)"},\
	{'eng_title':"CAMPOSANTO", 'han_title':"공동묘지",\
	'description':"죽은 모든 플레이어는 생명 1인채로 부활. 역할은 죽은 플레이어끼리 섞어서 나누어짐."},\
	{'eng_title':"REVEREND", 'han_title':"목사",\
	'description':"이번 라운드동안 맥주를 사용할 수 없다. 주점은 가능하다."},\
	{'eng_title':"CURSE", 'han_title':"저주",\
	'description':"전체 라운드 동안 모든 카드의 트럼프 무늬는 하트가 된다."},\
	{'eng_title':"Doctor", 'han_title':"의사",\
	'description':" 플레이어들 중 생명점이 가장 적은 플레이어들은 체력을 1 회복."},\
	{'eng_title':"Hangover", 'han_title':"만취",\
	'description':"모든 캐릭터의 특수능력이 일시적으로 사라진다."},\
	{'eng_title':"Train Arrival", 'han_title':"기차 도착",\
	'description':"자신의 턴을 시작할때 카드를 받는 단계후에 카드 한 장을 더 받는다."},\
	{'eng_title':"Shootout", 'han_title':"총격전",\
	'description':"턴당 뱅 카드를 쓸 수 있는 제한이 2장으로 늘어나게 된다."},\
	{'eng_title':"Thirst", 'han_title':"갈증",\
	'description':"자신의 턴에 카드 한장만 가져올 수 있게 된다."},\
	{'eng_title':"Handcuffs", 'han_title':"수갑",\
	'description':"(카드 가져오기) 가 끝나고, 각 플레이어는 카드 트럼프 무늬를 말한다(스페이드/다이아몬드/하트/클로버). 자신의 턴 동안에는 말한 무늬의 카드만 사용 가능하다."},\
	{'eng_title':"Hard Liquor", 'han_title':"중류주",\
	'description':"각 플레이어는 페이즈 1(카드 가져오기)를 생략하는 대신 체력을 1 포인트 회복할 수 있다. "},\
	{'eng_title':"Ranch", 'han_title':"목장",\
	'description':"(카드 가져오기)가 끝난 직후에, 단 한 번 원하는 수 만큼의 손 안의 카드를 버리고 같은 수의 카드를 카드더미에서 받아온다."},\
	{'eng_title':"Law Of The West", 'han_title':"서부의 법칙",\
	'description':"(카드 가져오기)를 할 때, 두번째로 가져온 카드를 보여주고, 사용 가능하다면 사용해야 한다."},\
	{'eng_title':"Lasso", 'han_title':"올가미",\
	'description':" 전체 라운드 동안 장착된 카드의 능력은 효과가 없다.(다이너마이트가 터져도 데미지X)"},\
	{'eng_title':"Abandoned Mine", 'han_title':"폐광",\
	'description':" (카드 가져오기) 때에는 버려진 카드에서 순차적으로 2장을 가져 온다. 단, 버려진 카드의 수가 페이즈 1을 시행하기에 부족하면 정상적으로 덱에서 가져온다."},\
	{'eng_title':"Judge", 'han_title':"심판",\
	'description':"전체 라운드 동안, 어느 누구에게도 카드를 장착할 수 없다."},\
	{'eng_title':"Peyote", 'han_title':"피요테 선인장",\
	'description':"(카드 가져오기)를 대신해서, 카드 더미에서 한 장을 뽑기 전에 트럼프 무늬의 색깔을 맞춘다(빨강/검정). 뽑은 후에 확인하여, 맞으면 계속 같은 방법으로 진행하며, 못 맞힌 경우에는 마지막으로 뽑은 카드는 버림."},\
	{'eng_title':"Blood Brothers", 'han_title':"피의 형제",\
	'description':"각 플레이어는 턴의 시작에 체력을 1 포인트(마지막 포인트 제외) 감소 시켜 원하는 (살아남은) 사람의 체력을 1 포인트 증가시킬 수 있다."},\
	{'eng_title':"Ricochet", 'han_title':"튕겨내기",\
	'description':"각 플레이어는 뱅 카드를 버리고 상대방의(거리 상관 없이) 장착중인 카드를 제거할 수 있다."},\
	{'eng_title':"Vendetta", 'han_title':"피의 복수",\
	'description':"각 플레이어는 턴의 끝에, 카드 펼치기를 시전한다. 하트가 나올 경우, 그는 한 번 더 턴을 진행한다."},\
	{'eng_title':"Miss Susanna", 'han_title':"미스 수잔나",\
	'description':"자신의 턴에, 반드시 카드를 3장 이상 사용해야 한다. 3장을 사용하지 못하면 그 플레이어는 라이프가 1 감소한다. "},\
	{'eng_title':"Lady Rose Of Texas", 'han_title':"텍사스의 레이디 로즈",\
	'description':"자신의 턴에, 자신의 오른쪽에 있는 플레이어와 자리를 바꿀 수 있다. "},\
	{'eng_title':"Helena Zontero", 'han_title':"헬레나 존테로",\
	'description':"이 카드가 발동되면, 카드 펼치기를 시전한다. 펼쳐진 카드의 무늬가 하트나 다이아몬드라면(즉, 무늬가 빨간색이라면), 보안관을 제외한 모든 플레이어의 직업을 섞어 랜덤으로 다시 나눠준다."},\
	{'eng_title':"Sacagaway", 'han_title':"새커거웨이",\
	'description':"모든 플레이어가 자신의 카드를 공개한 채로 진행한다."},\
	{'eng_title':"Darling Valentine", 'han_title':"내 사랑 발렌타인",\
	'description':"자신의 턴을 시작할 때, 자신의 손에 있는 카드를 버리고 그 수만큼 새로 카드를 가져온다."},\
	{'eng_title':"Showdown", 'han_title':"최후의 결전",\
	'description':"모든 카드는 뱅으로 여겨 사용할 수 있고, 모든 뱅은 빗나감으로만 여겨 사용할 수 있다. "},\
	{'eng_title':"Haze/Cloud", 'han_title':"안개",\
	'description':"각 플레이어는 다른 플레이어를 볼 때 거리가 1 멀어진다."},\
	{'eng_title':"Bucked Of", 'han_title':"낙마",\
	'description':"'야생마'를 장착하고 있는 플레이어들은 자기 차례 시작 전에 카드 펼치기를 시전한다. 그 문양이 하트가 아니었을 경우, 생명력을 1 잃고 야생마가 파괴된다."},\
	{'eng_title':"Saloon Dance", 'han_title':"파티 타임",\
	'description':"이 카드가 펼쳐졌을 때, 모든 플레이어는 카드 펼치기를 시전한다. 그 후, 하트 문양이 나온 사람들은 그 사람들끼리 시계방향으로 자리를 바꾼다."},\
	{'eng_title':"Betrayal", 'han_title':"배신",\
	'description':"이 카드가 펼쳐질 경우 보안관은 카드 펼치기를 한다. 스페이드 문양이 나오면 보안관을 제외한 모든 직업 카드를 섞어서 재분배한다."},\
	]

Last_list = [\
			{'eng_title':"PER UN PUGNO DI CARTE", 'han_title':"한 줌의 카드",\
			'description':"자신의 차례때, 자기가 든 패의 수만큼의 <뱅!> 공격을 받음."},\
			{'eng_title':"Final Hour", 'han_title':"최후의 시간",\
			'description':"모든 플레이어들 사이의 기본 거리는 1이 된다. 이는 장착 카드와 캐릭터 효과로 인하여 조정 가능하다. 각 플레이어는 자신의 차례에 결과적으로 공격을 하는 카드를 사용하거나 무기를 내려놓는 것 외에 아무것도 할 수 없다."},\
			{'eng_title':"Ataque Indio", 'han_title':"인디언의 대습격",\
			'description':"자신의 차례가 시작될 때 카드 펼치기를 한다. 만약 스페이드가 나오면 자신을 포함한 모든 플레이어에게 인디언의 효과가 발동된다. "},\
			{'eng_title':"WILD WEST SHOW", 'han_title':"와일드 웨스트 쇼",\
			'description':"모든 플레이어의 목적이 마지막에 홀로 살아남는 것으로 변경."},\
			{'eng_title':"High Noon", 'han_title':"하이 눈",\
			'description':"모든 플레이어는 자신의 턴이 시작할때 생명점을 하나를 줄이고 시작하게 된다."},\
			]