import random

#Initializations
alphabet = 'abcdefghijklmnopqrstuvwxyz'
inputmessage = 'ecosystem'
encoded_message = []
distorted_message = []
unicoded_distorted_message = []
error = 0.9

#Create enough dictionaries for length of input message
for x in range(1,len(inputmessage)+1):
    globals()['dict%s' % x] = {}

#----------------- Add Noise to message Start -----------
for char in inputmessage:
    encoded_message.append(ord(char) - 97)

for char in encoded_message:
    a = random.uniform(0, 1)
    if 25 >= char >= 0 and a > error:
        distorted_message.append((char + random.randrange(1, 25, 1)) % 26)
    else:
        distorted_message.append(char)

print(encoded_message)
print(distorted_message)

for char in distorted_message:
        unicoded_distorted_message.append(chr((char+97)))

unicoded_distorted_message[0] = inputmessage[0]
unicoded_distorted_message[len(inputmessage)-1] = inputmessage[len(inputmessage)-1]

outputmessage = ""
for element in unicoded_distorted_message:
    outputmessage = outputmessage + element

print(outputmessage)
#----------------- Add Noise to message End -----------


# I.I.D. Letter Distribution
singledist = {'f': 0.023797111389971804, 'o': 0.07616394698741859, 'u': 0.027312685479657234, 't': 0.0907077964750941, 'y': 0.01781333142234572, 's': 0.06593241955050579, 'b': 0.014404856638522912, 'j': 0.0012670792877423663, 'c': 0.028541177517493216, 'v': 0.010311851916309768, 'e': 0.12478211000594952, 'r': 0.06094324563658922, 'p': 0.01947337066321639, 'h': 0.058014945865632106, 'w': 0.019850974465871744, 'q': 0.0008999097924596576, 'z': 0.000747332656350221, 'k': 0.006457064400151357, 'm': 0.025015365994159152, 'n': 0.07264994788752525, 'x': 0.001931331232559449, 'i': 0.0719845147003641, 'g': 0.019080213836364074, 'd': 0.04246684351177049, 'a': 0.080342001158405, 'l': 0.03910857152757079}


# Transition matrix for block for order 1 Markov Chain
#transition = {'a': [{'y': 0.03298587385515194}, {'t': 0.1813690627685144}, {'a': 4.384753455869039e-05}, {'n': 0.26398408181059546}, {'o': 0.0003946278110282135}, {'j': 0.001049208862654377}, {'h': 0.0014250448731574375}, {'l': 0.10421932571249867}, {'e': 0.0029534446492032167}, {'z': 0.0016192268119173522}, {'g': 0.02333002035197748}, {'w': 0.011381567184734348}, {'r': 0.1269730641817048}, {'b': 0.024711217690576225}, {'i': 0.04935040014580603}, {'m': 0.03314873612636993}, {'x': 0.001766429249364384}, {'c': 0.05058439504695775}, {'u': 0.013508172610830831}, {'p': 0.0258011421210351}, {'d': 0.06017134528153998}, {'q': 3.7583601050306046e-05}, {'s': 0.12024559959369999}, {'f': 0.011513109788410419}, {'k': 0.013905932388613238}, {'v': 0.026377424003806462}], 'd': [{'l': 0.01241941343706343}, {'a': 0.02894505469468266}, {'w': 0.000687333949761144}, {'y': 0.011886137096731508}, {'i': 0.10321859831757868}, {'f': 0.0009184203639049769}, {'h': 0.0009776732906085237}, {'m': 0.004722458258272688}, {'c': 0.00013035643874780315}, {'v': 0.004562475356173111}, {'e': 0.16914932986061532}, {'s': 0.0286132383051428}, {'o': 0.05352909398398427}, {'d': 0.01252014341245946}, {'q': 0.0002903393408473798}, {'u': 0.022231698099170794}, {'t': 0.00040291990158411895}, {'k': 0.0005095751696505033}, {'j': 0.0022219847513830085}, {'z': 1.185058534070938e-05}, {'n': 0.0027137840430224475}, {'p': 7.702880471461097e-05}, {'g': 0.005237958720593546}, {'b': 0.00013628173141815787}, {'r': 0.03227506917542199}], 'j': [{'r': 0.0003971787385803383}, {'i': 0.003376019277932876}, {'a': 0.12491271328351639}, {'e': 0.3211190101422035}, {'u': 0.4410669891934657}, {'o': 0.3687804587718441}], 'y': [{'m': 0.013687950223231743}, {'k': 0.0005367823616953624}, {'a': 0.023787934134078696}, {'p': 0.0101564873173412}, {'b': 0.002387268924382007}, {'x': 0.0003955238454597408}, {'i': 0.025398281219164782}, {'s': 0.046516429396390224}, {'d': 0.002189507001652136}, {'t': 0.0154960592310477}, {'w': 0.0017657314529452711}, {'g': 0.0007204184328016706}, {'z': 0.00038139799383617856}, {'l': 0.0096338308072694}, {'h': 0.00025426532922411904}, {'n': 0.004590901777657705}, {'e': 0.06366521326739469}, {'f': 0.0016244729367096496}, {'c': 0.003955238454597407}, {'v': 7.062925811781085e-05}, {'r': 0.0031359390604308018}, {'u': 0.0008758028006608544}, {'o': 0.12823448103869736}], 'o': [{'l': 0.05019754391131507}, {'e': 0.003924883649245907}, {'j': 0.0012190926486294103}, {'s': 0.04313737862643417}, {'i': 0.01439124004723499}, {'p': 0.024193537848003176}, {'w': 0.05478318238366635}, {'x': 0.0015858115754528914}, {'o': 0.03747801356653667}, {'m': 0.07525006302935522}, {'c': 0.017044170662003057}, {'u': 0.13898316949198383}, {'q': 0.00012554341639002057}, {'k': 0.015022260903300621}, {'t': 0.055605822138432535}, {'g': 0.006353157624158147}, {'h': 0.0028082079981978287}, {'f': 0.14391570424646544}, {'r': 0.14519756860328983}, {'v': 0.03650670397657177}, {'y': 0.005044863074409512}, {'a': 0.007681274818599943}, {'d': 0.021127635468794252}, {'z': 0.0005253000843687704}, {'n': 0.21613290263776702}, {'b': 0.0073244672141230425}], 'w': [{'y': 0.0011408287755515425}, {'s': 0.016250472113967525}, {'t': 0.004081631841417741}, {'p': 0.00010140700227124821}, {'o': 0.10131827114426088}, {'m': 0.00011408287755515425}, {'d': 0.005881606131732397}, {'e': 0.1907085436463662}, {'a': 0.25624281886416034}, {'n': 0.05051336300636552}, {'u': 0.0005197108866401471}, {'c': 0.0003295727573815567}, {'w': 0.0005704143877757712}, {'h': 0.249676715467097}, {'r': 0.01295474454015196}, {'b': 0.00034224863266546274}, {'i': 0.2170616883616068}, {'l': 0.0051337294899819405}, {'f': 0.0011028011496998244}, {'k': 0.00098871827214467}], 'm': [{'n': 0.004184525874508204}, {'a': 0.21700186704510932}, {'l': 0.002404090586556396}, {'p': 0.08447511609163436}, {'t': 0.0006940679936083318}, {'r': 0.004979183432407598}, {'h': 5.02947821455313e-05}, {'y': 0.040789068320025886}, {'o': 0.13523261023290456}, {'u': 0.0390488688577905}, {'f': 0.0018910838086719766}, {'b': 0.03140406197166974}, {'g': 1.0058956429106259e-05}, {'i': 0.10939115116653057}, {'s': 0.036091535667633255}, {'e': 0.3205085287006127}, {'c': 0.0016194919850861078}, {'v': 2.0117912858212517e-05}, {'k': 7.041269500374382e-05}, {'d': 8.047165143285007e-05}, {'j': 1.0058956429106259e-05}, {'m': 0.03283243378460283}, {'w': 0.00012070747714927511}], 'f': [{'h': 4.2295633696017495e-05}, {'t': 0.044854519534626554}, {'f': 0.06630897972693144}, {'r': 0.1172646444222085}, {'s': 0.0022839642195849447}, {'k': 7.401735896803061e-05}, {'m': 3.172172527201312e-05}, {'w': 0.00033836506956813996}, {'a': 0.07779224427540017}, {'y': 0.002569459747033063}, {'e': 0.10668016208978014}, {'i': 0.10679647508244418}, {'u': 0.03713556638510336}, {'l': 0.029088822074436034}, {'j': 1.0573908424004374e-05}, {'o': 0.18441953682306028}, {'g': 2.1147816848008748e-05}, {'d': 1.0573908424004374e-05}, {'b': 0.00029606943587212245}, {'n': 0.0004335302453841793}], 'h': [{'y': 0.008249552858139506}, {'e': 0.6118244877613127}, {'s': 0.00224238634472036}, {'t': 0.029198732829124687}, {'a': 0.19041199791019056}, {'r': 0.013007575721114816}, {'p': 3.4698434734551023e-05}, {'c': 0.0003166232169527781}, {'q': 8.674608683637756e-06}, {'k': 0.0004163812168146123}, {'h': 6.939686946910205e-05}, {'f': 0.00042071852115643115}, {'b': 0.0006505956512728317}, {'g': 4.337304341818878e-06}, {'n': 0.001492032693585694}, {'u': 0.012422039634969266}, {'m': 0.0023464816489240127}, {'o': 0.09778018908196479}, {'w': 0.0006592702599564694}, {'i': 0.17224303002231128}, {'d': 0.0006072226078546428}, {'v': 3.90357390763699e-05}, {'l': 0.001600465302131166}], 'v': [{'i': 0.2228622846195676}, {'s': 0.006686112557293498}, {'u': 0.002122962746293921}, {'l': 0.005246402189117161}, {'w': 2.440187064705656e-05}, {'o': 0.0781347898118751}, {'k': 0.0001952149651764525}, {'g': 7.320561194116968e-05}, {'n': 0.012981795184234092}, {'v': 4.880374129411312e-05}, {'y': 0.006368888238881763}, {'a': 0.10778306264804884}, {'r': 0.002171766487588034}, {'e': 0.7584345415811651}, {'t': 4.880374129411312e-05}], 'e': [{'n': 0.1133095449268219}, {'r': 0.1712286897815679}, {'s': 0.09737078993302228}, {'g': 0.008616687764234028}, {'h': 0.0020205759746694347}, {'k': 0.001052635388001442}, {'v': 0.020102916059360872}, {'q': 0.002321040865114291}, {'d': 0.11037345848059565}, {'b': 0.0020286421462250015}, {'p': 0.014642117916242281}, {'u': 0.0028715570737817115}, {'e': 0.02956251875115161}, {'w': 0.010857066913792653}, {'i': 0.014043204678241461}, {'x': 0.014404165855353066}, {'t': 0.028987804027817487}, {'l': 0.0393467848480539}, {'m': 0.029016035628261973}, {'j': 0.000312564147778206}, {'a': 0.0556263355900762}, {'z': 0.0005222846082229378}, {'c': 0.029937595728485457}, {'f': 0.012790931544239745}, {'o': 0.006172637782897346}, {'y': 0.01321037246512921}], 'q': [{'u': 1.2756046437515804}], 'z': [{'n': 0.005723935740984192}, {'w': 0.0003367021024108348}, {'v': 0.0003367021024108348}, {'u': 0.05690265530743108}, {'z': 0.027946274500099285}, {'i': 0.1279467989161172}, {'k': 0.0013468084096433391}, {'o': 0.23670157799481684}, {'l': 0.02457925347599094}, {'e': 0.5346829386284057}, {'d': 0.009090956765092539}, {'m': 0.021212232451882588}, {'h': 0.051852123771268556}, {'y': 0.010774467277146713}, {'s': 0.0006734042048216696}, {'a': 0.10505105595218045}], 's': [{'t': 0.1471665343402888}, {'g': 0.000339664986807544}, {'a': 0.04906823298184936}, {'i': 0.0763559257422307}, {'y': 0.006724603446684185}, {'h': 0.06665066662479717}, {'l': 0.01092652648573032}, {'j': 1.9082302629637304e-05}, {'d': 0.0004427094210075854}, {'c': 0.020402797971608204}, {'e': 0.14223948380131646}, {'z': 1.526584210370984e-05}, {'u': 0.04742715495570055}, {'f': 0.002289876315556476}, {'k': 0.012956883485523728}, {'s': 0.07383706179511858}, {'m': 0.012357699182953118}, {'w': 0.005285797828409533}, {'r': 0.0002137217894519378}, {'b': 0.0019578442498007875}, {'q': 0.0010686089472596888}, {'n': 0.0022326294076675645}, {'o': 0.06317768754620318}, {'v': 0.000389278973644601}, {'p': 0.025936665734203022}], 'k': [{'o': 0.026460280557664733}, {'v': 0.00046763382428862565}, {'b': 0.0003117558828590838}, {'c': 0.001831565811797117}, {'r': 0.0045594297868141}, {'i': 0.209772739678806}, {'p': 7.793897071477095e-05}, {'u': 0.029227114018039103}, {'a': 0.032656428729489026}, {'m': 0.0023381691214431283}, {'y': 0.011184242297569631}, {'k': 3.896948535738547e-05}, {'h': 0.03230570336127256}, {'s': 0.060558580245377025}, {'q': 3.896948535738547e-05}, {'d': 0.0001558779414295419}, {'f': 0.0017536268410823462}, {'w': 0.004715307728243642}, {'l': 0.024862531658011933}, {'n': 0.11862311342788137}, {'t': 0.0007793897071477094}, {'e': 0.37293797487017893}, {'g': 0.0008183591925050949}], 'b': [{'e': 0.39604148548543977}, {'l': 0.150681627284642}, {'n': 0.0011354400386623846}, {'r': 0.08428458748532318}, {'j': 0.00841972459438876}, {'i': 0.04548747477964384}, {'d': 0.002183538535889201}, {'u': 0.15097858852552293}, {'c': 0.0027599927093639506}, {'a': 0.09951695231168624}, {'o': 0.14968593371227654}, {'k': 1.746830828711361e-05}, {'h': 5.240492486134083e-05}, {'v': 0.0021311336110278606}, {'b': 0.007319221172300603}, {'y': 0.12067107364738083}, {'t': 0.011389337003198073}, {'w': 0.00040177109060361303}, {'m': 0.002637714551354155}, {'p': 3.493661657422722e-05}, {'f': 1.746830828711361e-05}, {'s': 0.02864802559086632}], 'l': [{'k': 0.008634562767148683}, {'c': 0.0038604602535687103}, {'b': 0.0015120135993144117}, {'h': 0.0003410073223985694}, {'v': 0.00766301360333389}, {'l': 0.15970724069013756}, {'m': 0.007843168415167096}, {'e': 0.2116239970002141}, {'i': 0.14319733900570872}, {'r': 0.00427224268061604}, {'g': 0.0012096108794515292}, {'y': 0.12226077623052108}, {'d': 0.071971847327366}, {'n': 0.0017693776162189922}, {'u': 0.02751864750752229}, {'s': 0.025112293949464463}, {'o': 0.10864621973626874}, {'p': 0.004484567994562319}, {'q': 6.434100422614517e-06}, {'a': 0.13026479715625353}, {'t': 0.026161052318350628}, {'f': 0.019746254197003956}, {'w': 0.005160148538936844}, {'z': 0.00016728661098797747}], 'x': [{'x': 0.013419620959980373}, {'c': 0.1676801182086868}, {'h': 0.015895085020559276}, {'y': 0.005732653613972198}, {'p': 0.28702354344501707}, {'w': 0.00013028758213573177}, {'t': 0.19699482418922643}, {'a': 0.1338053468533965}, {'r': 0.00013028758213573177}, {'e': 0.10852955591906456}, {'q': 0.0009120130749501224}, {'u': 0.014983071945609154}, {'v': 0.015243647109880618}, {'s': 0.0016937385677645131}, {'i': 0.16090516393762871}, {'l': 0.0005211503285429271}, {'o': 0.013680196124251837}, {'f': 0.0018240261499002449}], 'i': [{'v': 0.027849379569539895}, {'m': 0.05298268433984137}, {'a': 0.031047846031963523}, {'t': 0.1559593220628332}, {'j': 6.99118352442322e-06}, {'o': 0.08886493377894354}, {'g': 0.03213497507001133}, {'q': 0.00044044456203866286}, {'u': 0.0018631504092587881}, {'z': 0.005121041931640009}, {'x': 0.0026391717804697657}, {'e': 0.053674811508759274}, {'d': 0.05075249679555037}, {'h': 9.088538581750186e-05}, {'y': 3.49559176221161e-06}, {'w': 1.747795881105805e-05}, {'f': 0.02564016557582216}, {'b': 0.011346690860138887}, {'i': 0.002034434405607157}, {'n': 0.3434768465549128}, {'c': 0.07883258542139623}, {'s': 0.16355873855388123}, {'l': 0.05790797313279753}, {'r': 0.042149845468747595}, {'k': 0.006725518550495137}, {'p': 0.009147963641707783}], 'n': [{'j': 0.002348303227890066}, {'r': 0.0008624299465259977}, {'o': 0.07030016315115734}, {'z': 0.00015239725962708394}, {'c': 0.056657144840450896}, {'i': 0.04603436312962665}, {'a': 0.04082168413556389}, {'h': 0.001239959521511274}, {'e': 0.10236939558041121}, {'g': 0.15098065782736855}, {'q': 0.0012676681141707438}, {'f': 0.010006265524151035}, {'y': 0.01307845573526975}, {'p': 0.0004952910937880228}, {'w': 0.0007758405944651547}, {'l': 0.01188005910274768}, {'n': 0.011679171805966523}, {'t': 0.1250038522091156}, {'u': 0.00920271633702641}, {'s': 0.055763542727182994}, {'m': 0.0029925280072227393}, {'d': 0.2192892658811265}, {'v': 0.005895003088302202}, {'b': 0.0013888932070559243}, {'x': 0.0006892512424043115}, {'k': 0.009105736262718267}], 't': [{'b': 0.0001276065605504401}, {'n': 0.0008544091445551206}, {'c': 0.0033566073536094028}, {'y': 0.018677716786654634}, {'h': 0.4142525063816907}, {'t': 0.022012131694950914}, {'a': 0.05251842183349852}, {'g': 0.00019973200781808016}, {'p': 0.0002663093437574402}, {'x': 2.2192445313120018e-05}, {'r': 0.039205728701290646}, {'s': 0.02835362294317496}, {'k': 3.051461230554002e-05}, {'i': 0.11750622387730635}, {'l': 0.014988222753348431}, {'v': 4.993300195452004e-05}, {'d': 4.1610834962100026e-05}, {'e': 0.1208739274535723}, {'u': 0.025338224436254782}, {'f': 0.0008710534785399607}, {'z': 0.0003994640156361603}, {'o': 0.12111804435201663}, {'w': 0.006885206158395486}, {'m': 0.002826762721758662}], 'c': [{'w': 6.171431907720595e-05}, {'n': 7.934698167069337e-05}, {'y': 0.012475108784892346}, {'m': 0.00014987763204464302}, {'i': 0.06784166932844282}, {'f': 0.00010579597556092448}, {'h': 0.1890485919960753}, {'e': 0.22409350890063157}, {'t': 0.11671941003758993}, {'u': 0.05100247655166234}, {'q': 0.0020630215234380272}, {'c': 0.027048504418409693}, {'o': 0.2576484658160381}, {'r': 0.04347332962424322}, {'d': 0.0004937145526176476}, {'a': 0.15783877920560258}, {'k': 0.044989738607283135}, {'l': 0.048075454561143434}, {'z': 0.00022040828241859267}, {'s': 0.00354416518129097}], 'r': [{'h': 0.0028448110789287954}, {'d': 0.029984061037998423}, {'m': 0.02950923770842395}, {'z': 0.00035095637403330566}, {'w': 0.00219657401159669}, {'i': 0.11743826054858016}, {'o': 0.12283885981017502}, {'g': 0.016371082624024202}, {'p': 0.005474919434919569}, {'u': 0.02332414772840169}, {'x': 8.25779703607778e-06}, {'k': 0.009760716096643937}, {'s': 0.06533981904796543}, {'c': 0.01656101195585399}, {'a': 0.09536516907114424}, {'j': 1.651559407215556e-05}, {'f': 0.005809360214880719}, {'r': 0.032915578985806035}, {'n': 0.024868355774148237}, {'y': 0.048159472314405614}, {'l': 0.011556786951990855}, {'b': 0.003001709222614273}, {'t': 0.04901415430763967}, {'v': 0.009240474883371036}, {'e': 0.3022931760996993}, {'q': 0.00010322246295097226}], 'u': [{'l': 0.13276680460031054}, {'x': 0.0007554561083356785}, {'r': 0.18917726498249784}, {'p': 0.05738702559540173}, {'e': 0.04788854696498607}, {'n': 0.15787190088341693}, {'i': 0.03043014055893593}, {'z': 0.006495079955812846}, {'g': 0.052301516183190816}, {'f': 0.008365294467912147}, {'b': 0.03042092767956598}, {'s': 0.17742163090644508}, {'a': 0.031775220946948235}, {'d': 0.022626831732590568}, {'o': 0.002773076690354137}, {'t': 0.17885884008815686}, {'w': 1.84257587398946e-05}, {'y': 0.0007093917114859421}, {'k': 0.002478264550515824}, {'u': 9.2128793699473e-06}, {'h': 0.00043300533038752304}, {'v': 0.00092128793699473}, {'q': 7.37030349595784e-05}, {'j': 9.2128793699473e-06}, {'m': 0.04204758144443948}, {'c': 0.049648206924646}], 'g': [{'r': 0.09565203809475048}, {'l': 0.04290032812935658}, {'y': 0.003296981872837118}, {'o': 0.07262591669485605}, {'t': 0.00673903094807907}, {'f': 0.00011869134742213626}, {'s': 0.020032461859358332}, {'i': 0.07067410342613646}, {'a': 0.08444229972710428}, {'n': 0.02910575597340608}, {'g': 0.011882322669704974}, {'e': 0.17367181713356805}, {'h': 0.13405528294955724}, {'b': 3.956378247404542e-05}, {'u': 0.03748008993041236}, {'z': 3.956378247404542e-05}, {'k': 7.912756494809083e-05}, {'d': 0.0008308394319549538}, {'w': 0.0003296981872837119}, {'m': 0.002571645860812952}], 'p': [{'m': 0.002067467258300169}, {'k': 0.0003618067702025296}, {'n': 0.0006719268589475549}, {'s': 0.026437737565513406}, {'o': 0.15339314889550815}, {'u': 0.05195803653515612}, {'p': 0.07789182895645887}, {'a': 0.1502919480080579}, {'w': 0.000697770199676307}, {'b': 0.00042641512202440987}, {'r': 0.21325924769366242}, {'c': 0.0017315038288263915}, {'g': 0.0003488850998381535}, {'d': 0.00010337336291500844}, {'i': 0.08945672393257544}, {'l': 0.11712202018270457}, {'h': 0.03314408448462458}, {'e': 0.22468200429577084}, {'f': 0.0017056604880976395}, {'t': 0.04702195845596447}, {'y': 0.008567067451581326}]}

#Peter Pan
transition = {'a': [{'c': 0.036936186284845976}, {'b': 0.027423618587356643}, {'e': 0.0093411700813183576}, {'d': 0.079014301054821323}, {'g': 0.025709642425646852}, {'f': 0.0084841820004634607}, {'i': 0.080299783176103673}, {'h': 0.0013711809293678323}, {'k': 0.016882665192841435}, {'j': 8.569880808548952e-05}, {'m': 0.029137594749066437}, {'l': 0.077643120125453505}, {'o': 0.00059989165659842653}, {'n': 0.24578418158918391}, {'p': 0.023824268647766083}, {'s': 0.15502914382665053}, {'r': 0.13300455014867973}, {'u': 0.012254929556225}, {'t': 0.1658271936454222}, {'w': 0.018168147314123775}, {'v': 0.040192740992094578}, {'y': 0.044477681396369061}, {'x': 0.00034279523234195808}, {'z': 0.0019710725859662585}], 'c': [{'k': 0.10597639902063596}, {'i': 0.046090327384714455}, {'h': 0.2627462200570797}, {'o': 0.22010482873516699}, {'l': 0.052988199510317982}, {'c': 0.02069361637681057}, {'a': 0.17307388242423388}, {'f': 0.021320695660956346}, {'e': 0.17589573920288984}, {'y': 0.0043895549890204241}, {'s': 0.002194777494510212}, {'r': 0.11005241436758349}, {'q': 0.0012541585682915499}, {'p': 0.00062707928414577495}, {'u': 0.04201431203776692}, {'t': 0.071800578034691226}], 'b': [{'e': 0.41876811840566203}, {'a': 0.081578204884219879}, {'b': 0.011295443753199675}, {'l': 0.10124064401016006}, {'m': 0.00083669953727405}, {'o': 0.18114544981983183}, {'i': 0.056477218765998378}, {'j': 0.0041834976863702501}, {'t': 0.0083669953727405003}, {'u': 0.22800062390717862}, {'v': 0.000418349768637025}, {'r': 0.076976357429212591}, {'s': 0.027192734961406624}, {'y': 0.076558007660575578}], 'e': [{'m': 0.027051864608186791}, {'l': 0.04510388257689945}, {'o': 0.0020406629008109961}, {'n': 0.10894000408944855}, {'i': 0.015383458790729047}, {'h': 0.0013081172441096129}, {'k': 0.0010988184850520748}, {'j': 0.00036627282835069159}, {'e': 0.04510388257689945}, {'d': 0.11548059030999662}, {'g': 0.0042382998709151456}, {'f': 0.011354457678871438}, {'a': 0.057975756258938041}, {'c': 0.015906705688372894}, {'b': 0.00020929875905753806}, {'y': 0.036836581594126699}, {'x': 0.0085812491213590608}, {'z': 0.00026162344882192255}, {'u': 0.00026162344882192255}, {'t': 0.051173546589568047}, {'w': 0.010726561401698824}, {'v': 0.022447291908920957}, {'q': 0.00047092220787946058}, {'p': 0.011982353956044052}, {'s': 0.06760349917558478}, {'r': 0.18350268700369649}], 'd': [{'n': 0.0024161549747684307}, {'o': 0.072342522479831264}, {'l': 0.012080774873842156}, {'m': 0.0029846620276551207}, {'j': 0.00014212676322167243}, {'k': 0.00028425352644334485}, {'h': 0.00028425352644334485}, {'i': 0.067225959003851046}, {'f': 0.0024161549747684307}, {'g': 0.0029846620276551207}, {'d': 0.013217788979615534}, {'e': 0.10588443860014594}, {'c': 0.00028425352644334485}, {'a': 0.046333324810265211}, {'y': 0.065378311081969315}, {'v': 0.005685070528866896}, {'w': 0.00028425352644334485}, {'t': 0.00042638028966501725}, {'u': 0.0041216761334285004}, {'r': 0.039369113412403262}, {'s': 0.029135986460442843}], 'g': [{'w': 0.00063382690915451706}, {'u': 0.027254557093644233}, {'t': 0.0012676538183090341}, {'s': 0.035494306912652956}, {'r': 0.061481210187988161}, {'z': 0.00031691345457725853}, {'y': 0.0019014807274635513}, {'g': 0.01996554763836729}, {'e': 0.14261105455976636}, {'b': 0.00063382690915451706}, {'a': 0.088418853827055124}, {'o': 0.096658603646063865}, {'n': 0.014261105455976635}, {'m': 0.00095074036373177565}, {'l': 0.038346528003848288}, {'i': 0.041832576004198124}, {'h': 0.24148805238787102}], 'f': [{'p': 0.00033518767502329169}, {'r': 0.072065350130007699}, {'s': 0.022122386551537251}, {'t': 0.069048661054798094}, {'u': 0.065696784304565159}, {'y': 0.0013407507000931667}, {'a': 0.11899162463326854}, {'c': 0.00067037535004658337}, {'e': 0.088489546206149003}, {'f': 0.043574397753027912}, {'i': 0.10726005600745332}, {'l': 0.066031971979588461}, {'m': 0.00033518767502329169}, {'o': 0.23630731089142062}], 'i': [{'x': 0.0023451790692389741}, {'z': 0.0028550006060300555}, {'q': 0.00020392861471643257}, {'p': 0.01009446642846341}, {'s': 0.15376217549619015}, {'r': 0.074433944371497876}, {'u': 0.0010196430735821627}, {'t': 0.1786414664915949}, {'w': 0.00010196430735821629}, {'v': 0.014580895952224927}, {'i': 0.00030589292207464883}, {'k': 0.013357324263926332}, {'m': 0.073618229912632144}, {'l': 0.069641621925661715}, {'o': 0.024777326688046556}, {'n': 0.35932221913035411}, {'a': 0.005913929826776544}, {'c': 0.059751084111914737}, {'b': 0.0099925021211051939}, {'e': 0.054448940129287492}, {'d': 0.074230015756781453}, {'g': 0.061382513029646202}, {'f': 0.027632327294076612}], 'h': [{'y': 0.004658942336583048}, {'r': 0.010231402778378458}, {'s': 0.0013702771578185434}, {'w': 0.00018270362104247248}, {'t': 0.055633252607432869}, {'u': 0.01333736433610049}, {'h': 9.1351810521236241e-05}, {'i': 0.17110194110627547}, {'n': 0.012606549851930601}, {'o': 0.10057834338388109}, {'l': 0.00073081448416988993}, {'m': 0.00045675905260618113}, {'b': 0.00036540724208494497}, {'a': 0.20846483160946108}, {'f': 0.00073081448416988993}, {'d': 0.00036540724208494497}, {'e': 0.64750163297452246}], 'k': [{'b': 0.0013319920271779853}, {'a': 0.0013319920271779853}, {'f': 0.00066599601358899264}, {'e': 0.41291752842517537}, {'i': 0.18381489975056195}, {'o': 0.0013319920271779853}, {'n': 0.16516701137007017}, {'l': 0.031967808652271647}, {'s': 0.031967808652271647}, {'w': 0.0019979880407669779}, {'u': 0.0013319920271779853}, {'y': 0.013319920271779851}], 'j': [{'u': 0.33858848428082722}, {'o': 0.57398809716178334}, {'e': 0.067717696856165452}, {'a': 0.12576143701859299}], 'm': [{'e': 0.35634071635084552}, {'f': 0.0027364048183938648}, {'a': 0.14715777023362564}, {'c': 0.00030404497982154059}, {'b': 0.027668093163760194}, {'m': 0.015810338950720107}, {'l': 0.0039525847376800267}, {'o': 0.15415080476952106}, {'n': 0.0057768546166092711}, {'i': 0.11736136221111465}, {'u': 0.046518881912695702}, {'t': 0.00091213493946462176}, {'p': 0.04530270199340955}, {'s': 0.031012587941797138}, {'r': 0.035877307618941784}, {'y': 0.030708542961975598}], 'l': [{'f': 0.015721225557400364}, {'g': 0.00032752553244584095}, {'d': 0.10922976507068793}, {'e': 0.1904560971172565}, {'b': 0.00016376276622292047}, {'c': 0.00098257659733752274}, {'a': 0.10546322144756078}, {'n': 0.00016376276622292047}, {'o': 0.10267925442177113}, {'l': 0.19258501307815448}, {'m': 0.0070417989475855796}, {'k': 0.0060592223502480566}, {'i': 0.16015998536601619}, {'v': 0.0049128829866876139}, {'w': 0.0094982404409293866}, {'t': 0.014247360661394079}, {'u': 0.015066174492508681}, {'r': 0.0032752553244584088}, {'s': 0.017195090453406649}, {'p': 0.0067142734151397392}, {'y': 0.17489863432607905}], 'o': [{'o': 0.078921974007690979}, {'n': 0.15143734071358114}, {'m': 0.062580482919039657}, {'l': 0.026926320543800449}, {'k': 0.038068246286062701}, {'i': 0.014205955321384373}, {'h': 0.018569876237103759}, {'g': 0.005013866584018015}, {'f': 0.090342447893509786}, {'e': 0.0046424690592759398}, {'d': 0.018198478712361681}, {'c': 0.01374170841545678}, {'b': 0.0056638122523166466}, {'a': 0.0087278418314387669}, {'z': 0.00074279504948415037}, {'y': 0.016341491088651308}, {'x': 0.00055709628711311278}, {'w': 0.079293371532433043}, {'v': 0.01838417747473272}, {'u': 0.20965390271690143}, {'t': 0.084864334403564182}, {'s': 0.02590497735075974}, {'r': 0.12014709925406131}, {'q': 9.2849381185518796e-05}, {'p': 0.015134449133239565}], 'n': [{'h': 0.001215900978937702}, {'i': 0.039516781815475313}, {'j': 0.00030397524473442549}, {'k': 0.024520669741910323}, {'l': 0.016009362889346408}, {'m': 0.00070927557104699277}, {'n': 0.011044433892017459}, {'o': 0.10993771351228389}, {'a': 0.030600174636598837}, {'b': 0.00070927557104699277}, {'c': 0.032322701023427249}, {'d': 0.26486376324526273}, {'e': 0.10932976302281504}, {'f': 0.011753709463064452}, {'g': 0.18816067649060939}, {'x': 0.0010132508157814182}, {'y': 0.011145758973595602}, {'z': 0.00010132508157814183}, {'p': 0.00020265016315628367}, {'q': 0.00070927557104699277}, {'r': 0.00010132508157814183}, {'s': 0.034855828062880789}, {'t': 0.081769340833560453}, {'u': 0.0094232325867671905}, {'v': 0.0025331270394535455}, {'w': 0.00070927557104699277}], 'q': [{'u': 0.97051875775523511}, {'j': 0.35481330928686017}], 'p': [{'r': 0.10529478692144253}, {'s': 0.028051506940461525}, {'p': 0.075617105665591933}, {'w': 0.000813087157694537}, {'t': 0.058542275354006662}, {'u': 0.041467445042421384}, {'y': 0.01057013305002898}, {'b': 0.000813087157694537}, {'a': 0.18782313342743803}, {'g': 0.0004065435788472685}, {'e': 0.35613217507020717}, {'h': 0.0073177844192508328}, {'i': 0.10610787407913708}, {'n': 0.000813087157694537}, {'o': 0.094318110292566301}, {'l': 0.091878848819482675}], 's': [{'y': 0.0032718862747912161}, {'s': 0.040244201179931959}, {'r': 0.00054531437913186932}, {'q': 0.0015268802615692341}, {'p': 0.02224882666858027}, {'w': 0.012215042092553873}, {'u': 0.031082919610516551}, {'t': 0.15323334053605528}, {'k': 0.013850985229949481}, {'i': 0.044606716212986917}, {'h': 0.11789696876831014}, {'o': 0.064892411116692458}, {'n': 0.0061075210462769366}, {'m': 0.013414733726643984}, {'l': 0.027920096211551712}, {'c': 0.016904745753087948}, {'b': 0.00032718862747912163}, {'a': 0.073290252555323246}, {'g': 0.00054531437913186932}, {'f': 0.00065437725495824325}, {'e': 0.11898759752657388}, {'d': 0.00065437725495824325}], 'r': [{'t': 0.043487269177233542}, {'u': 0.018896974907098699}, {'v': 0.0031494958178497827}, {'w': 0.0023015546361209952}, {'p': 0.0052087815449054099}, {'q': 0.00012113445453268396}, {'r': 0.019987184997892853}, {'s': 0.070742521447087439}, {'y': 0.043850672540831595}, {'d': 0.050634201994661898}, {'e': 0.30114025396825234}, {'f': 0.0032706302723824669}, {'g': 0.013324789998595236}, {'a': 0.06904663908362986}, {'b': 0.0037551680905132025}, {'c': 0.006177857181166882}, {'l': 0.031252689269432463}, {'m': 0.016474285816445017}, {'n': 0.019744916088827488}, {'o': 0.098603445989604743}, {'h': 0.004845378181307358}, {'i': 0.090487437535914914}, {'k': 0.011871176544203027}], 'u': [{'z': 0.0022060271136265688}, {'t': 0.25638937342815454}, {'v': 0.00024511412373628543}, {'p': 0.062013873305280208}, {'s': 0.15025495785034296}, {'r': 0.16692271826441035}, {'m': 0.017893331032748837}, {'l': 0.17084454424419093}, {'o': 0.00073534237120885635}, {'n': 0.1343225398074844}, {'i': 0.040688944540223385}, {'k': 0.0024511412373628542}, {'e': 0.03039415134329939}, {'d': 0.020099358146375406}, {'g': 0.071818438254731623}, {'f': 0.0044120542272531376}, {'a': 0.012010592063077984}, {'c': 0.044120542272531378}, {'b': 0.015687303919122268}], 't': [{'y': 0.0067372937911493501}, {'w': 0.0078010770213308269}, {'t': 0.023545068828016678}, {'u': 0.013971019756383389}, {'r': 0.027516526220694192}, {'s': 0.01255264211614142}, {'n': 0.00021275664603629527}, {'o': 0.12815041979586184}, {'l': 0.027658363984718385}, {'m': 0.00042551329207259054}, {'h': 0.44693079444024425}, {'i': 0.070635206484050028}, {'f': 0.0035459441006049212}, {'g': 0.00021275664603629527}, {'e': 0.12084577494861572}, {'b': 0.00028367552804839369}, {'c': 0.004680646212798496}, {'a': 0.0359558731801339}], 'w': [{'n': 0.038654536545421239}, {'f': 0.0054210630521017581}, {'e': 0.26751767670154331}, {'d': 0.0023569839356964166}, {'c': 0.0002356983935696417}, {'b': 0.0002356983935696417}, {'a': 0.33681300441101802}, {'o': 0.10606427710633877}, {'l': 0.0070709518070892503}, {'k': 0.0011784919678482083}, {'i': 0.16428178031804025}, {'h': 0.20505760240558826}, {'w': 0.0002356983935696417}, {'u': 0.00070709518070892507}, {'s': 0.0098993325299249514}, {'r': 0.0073066502006588919}], 'v': [{'i': 0.094050257361711187}, {'o': 0.051770783868831841}, {'u': 0.00086284639781386411}, {'a': 0.050045091073204116}, {'e': 1.1191117779645816}, {'y': 0.0077656175803247768}], 'y': [{'i': 0.029140735252919537}, {'m': 0.0011427739314870406}, {'l': 0.0022855478629740813}, {'o': 0.17170178320592785}, {'n': 0.00057138696574352032}, {'a': 0.0034283217944611217}, {'e': 0.050853439951173307}, {'d': 0.00028569348287176016}, {'f': 0.00028569348287176016}, {'p': 0.0014284674143588006}, {'s': 0.059709937920197874}, {'r': 0.00028569348287176016}, {'t': 0.0077137240375375242}, {'w': 0.00085708044861528042}], 'x': [{'h': 0.012805140744368072}, {'i': 0.083233414838392458}, {'o': 0.006402570372184036}, {'c': 0.30732337786483371}, {'a': 0.1472591185602328}, {'e': 0.057623133349656318}, {'y': 0.006402570372184036}, {'p': 0.28171309637609754}, {'q': 0.019207711116552107}, {'t': 0.21128482228207318}, {'u': 0.038415422233104214}], 'z': [{'l': 0.17476906378577081}, {'o': 0.029128177297628469}, {'i': 0.14564088648814233}, {'e': 0.59712763460138352}, {'a': 0.16020497513695656}, {'y': 0.029128177297628469}, {'z': 0.17476906378577081}]}


# Access probability from transition matrix corresponding to letter1 and letter2
def find_value(letter1, letter2, transition):
    for subletter in transition[letter1]:
         if list(subletter.keys())[0] == letter2:
              return list(subletter.values())[0]
    return 0

# Channel error for letter1 and letter2
def errormatrix(letter1, letter2):
    if letter1 == letter2:
        return error
    else:
        return (1-error)/25

# Find letter that corresponds to maximum probability value of dict within dict
def max_letter(dictstruct, letter):
    maxkey = ''
    maxvalue = 0
    for element in dictstruct.keys():
        if dictstruct[element][letter] > maxvalue:
            maxvalue = dictstruct[element][letter]
            maxkey = element
        else:
            continue
    return maxkey

# Find letter that corresponds to maximum probability value of dict
def single_max_letter(dictstruct):
    maxkey = ''
    maxvalue = 0
    for element in dictstruct.keys():
        if dictstruct[element] > maxvalue:
            maxvalue = dictstruct[element]
            maxkey = element
        else:
            continue
    return maxkey


#Verturbi Algorithm
def verturbi(transition, singledist, outputmessage, alphabet):
    for letter in alphabet:
        dict1[letter] = singledist[letter]*errormatrix(letter, outputmessage[0])
    print(dict1)
    for letter in alphabet:
        for letter2 in alphabet:
            if letter not in dict2.keys():
                dict2[letter] = {letter2 : dict1[letter]*find_value(letter, letter2, transition)*errormatrix(letter2, outputmessage[1])}
            else:
                dict2[letter][letter2] = dict1[letter]*find_value(letter, letter2, transition)*errormatrix(letter2, outputmessage[1])
    print(dict2)
    for i in range(3, len(inputmessage)+1):
        j = i-1
        for letter in alphabet:
            for letter2 in alphabet:
                if letter not in globals()['dict%s' % i].keys():
                    globals()['dict%s' % i][letter] = {letter2: globals()['dict%s' % j][max_letter(globals()['dict%s' % j], letter)][letter] * find_value(letter, letter2,transition) * errormatrix(letter2, outputmessage[j])}
                else:
                    globals()['dict%s' % i][letter][letter2] = globals()['dict%s' % j][max_letter(globals()['dict%s' % j], letter)][letter] * find_value(letter, letter2,transition) * errormatrix(letter2, outputmessage[j])
        print(globals()['dict%s' % i])

# Call Verturbi
verturbi(transition, singledist, outputmessage, alphabet)

# Find best path across nodes
nodes = {}
i = len(inputmessage)
for letter in alphabet:
    globals()['dict%s' % i][max_letter(globals()['dict%s' % i], letter)][letter]
    nodes[letter] = globals()['dict%s' % i][max_letter(globals()['dict%s' % i], letter)][letter]
print (nodes)

# Assign corresponding characters to maxletter(i)
globals()['maxletter%s' % i] = single_max_letter(nodes)
for i in range(len(inputmessage),1,-1):
    j = i - 1
    globals()['maxletter%s' % j] = max_letter(globals()['dict%s' % i],globals()['maxletter%s' % i])

# Put together word
word=""
for i in range(1,len(inputmessage)+1):
    word = word + globals()['maxletter%s' % i]
print(word)

