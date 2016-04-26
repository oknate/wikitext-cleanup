#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import collections
from AppKit import NSPasteboard,NSObject,NSStringPboardType

def sendToClipBoard(string):
    pasteboard = NSPasteboard.generalPasteboard()
    emptyOwner = NSObject.alloc().init()
    pasteboard.declareTypes_owner_([NSStringPboardType], emptyOwner)
    pasteboard.setString_forType_(string, NSStringPboardType)

def replaceRomanNumerals(string):
    dict = collections.OrderedDict()
    dict['VIII'] = '8'
    dict['VII'] = '7'
    dict['VI'] = '6'
    dict['IV'] = '4'
    dict['V'] = '5' 
    dict['IX'] = '9' 
    dict['X'] = '10'
    dict['III'] = '3' 
    dict['II'] = '2' 
    dict['I'] = '1'
    for i, v in dict.items():
        string = string.replace(str(i), str(v))
    return string

def replaceRomanNumerals(string):
    dict = collections.OrderedDict()
    dict['VIII'] = '8'
    dict['VII'] = '7'
    dict['VI'] = '6'
    dict['IV'] = '4'
    dict['V'] = '5' 
    dict['IX'] = '9' 
    dict['X'] = '10'
    dict['III'] = '3' 
    dict['II'] = '2' 
    dict['I'] = '1'
    for i, v in dict.items():
        string = string.replace(str(i), str(v))
    return string

def replaceRomanNumeralsOrdinal(string):
    dict = collections.OrderedDict()
    dict['VIII'] = 'the eighth'
    dict['VII'] = 'the seventh'
    dict['VI'] = 'the sixth'
    dict['IV'] = 'the fourth'
    dict['V'] = 'the fifth' 
    dict['IX'] = 'the ninth' 
    dict['X'] = 'the tenth'
    dict['III'] = 'the third' 
    dict['II'] = 'the second' 
    dict['I'] = 'the first'
    for i, v in dict.items():
        string = string.replace(str(i), str(v))
    return string
    

filename = '/Users/oknate2/Downloads/sample.txt'

searchreplace1  = {
  'é ' : 'ay ',
  'mise en scène' : 'me zon sen',
  'née' : 'nay',
  'naïve' : 'naive',
  'René Descartes' : 'run "A" day cart',
  'Blaise Pascal' : 'Blaze poz cal',
  'Jean-Jacques Rousseau' : 'John Jacques Rooso',
  'Françoise' : 'frons was',
  'de la ' : 'duh la',
  'Château' : 'shat toe',
  ' des ' : ' day ',
  'Guillaume' : 'ghee yome',
  'Peña' : 'Pain yah',
  'Iñárritu' : 'een ya re two',
  'González' : 'goensa less',
  'Zoë' : 'zo E',
  'Joan Miró' : 'jewan mi-roh',
  'Slavoj Žižek' : 'slah-voi zhe-zhek',
  'Étienne' : 'et tea yen',
  'Cuarón' : 'qua rone',
}

searchreplace2  = {
  'Fiennes' : 'Fines',
  'Alicia Vikander' : 'ah lissia vickander',
  'Vikander' : 'vickander',
  'Redmayne' : 'Red main',
  'tbsp' : 'table spoon',
  'Charlize' : 'shar lease',
  '[T]he' : 'The',
  'Alejandro' : 'ah lay hondro',
  'Ralph Fines' : 'Rafe Fines',
  'Scorsese' : 'Score Sazie',
  'Anthony Hopkins' : 'Ann tonnie Hopkins',
  'André Gide' : 'On dray jeed',
  'Andre Gide' : 'On dray jeed',
  'Fernando' : 'Fair nondo',
  'Julio' : 'who leo',
  'Castillo' : 'Cass tea oh',
  'Dalí' : 'Doll E',
  'Moebius' : 'murbi use',
  'sangre' : 'sahn gray',
  'Santa' : 'sahn tah',
  'Laurentiis' : 'lowren tiss',
  'Fransoise' : 'Fran swa',
  'Blanchett' : 'Blan shet',
  'Thomas Hobbes' : 'Thomas Hobs',
  'Andree' : 'on dray',
  'Breton' : 'brutone',
  'Mme ' : "ma dom",
  "Mlle " : 'Mod ma zell',
  'temps' : 'tom',
  'Chiwetel' : 'Chewy tell',
  'Ejiofor' : 'Edge E oh four',
  'Nolte': 'noll tea',
  'Baruchel' : 'Baroo shell',
  'Rene Descartes' : 'rennay day cart',
  'Descartes' : 'day cart',
  'Theroux' : 'Thero',
  'Pantoliano' : 'pant O lea on O',
  'Warner Bros.' : 'Warner Brothers',
  'Galifianakis' : 'gall lif fee a nakis',
  'Mathieu' : 'Matt hew',
  'Genghis Khan' : 'Gang gus Con',
  'Barthes' : 'Bart',
  'Haneke' : 'Haneka',
  'Nicodemus' : 'Nickadeemus',
  'Richard III' : 'Richard the third',
  'Von Trier' : 'von treer',
  'DVD' : 'Dee Vee Dee',
  'Kylo' : 'Kai lo',
  'Cuaron' : 'qua rone',
  'Alfonso' : 'all-fawn-so',
  'Chewbacca' : 'Chew bocka',
  'Kasdan' : 'Kazden',
  'Sidious' : 'sid dee us',
  'Anakin' : 'Anna kin',
  'Jedi' : 'Jeddeye',
  'Dameron' : 'demer ron',
  'Kanata' : 'kan notta',
  'von Trier' : 'von treer',
  'Jean Genet' : 'John \'ngine nay',
  'Genet' : '\'ngine nay',
  'Cassavetes' : 'Cassa vet ease',
  'Friedrich' : 'free drish',
  'Wilhelm' : 'Vil hailm',
  'Dürrenmatt' : 'durenmott',
  'Arrabal' : 'Ah rah ball',
  'Palahniuk' : 'pahl-uh-nik',
  'Picoult' : 'pee-coe',
  'Havel' : 'Hov vell',
  'Albert Camus' : 'All bear commu',
  'François Truffaut' : 'Frons wah tru fo',
  'Truffaut' : 'tru fo',
  'Jodorowsky' : 'hoeder offsky',
  'phoneticist' : 'phonetisist',
  'Simone de Beauvoir' : 'See moan duh Bove wahr',
  'Beauvoir' : 'Bove wahr',
  'cliché' : 'klee shay',
  "bipolarity" : "by polarity",
  "oxymoronic" : 'ocksie moronic',
  "Gena Rowlands" : "Jeana Rowlands",
  'Raimi' : 'ray me',
  'Anschluss' : 'on schluss',
  'rima facie' : 'rima fasha',
  ' Lorre' : ' Lorrie',
  'Americain' : 'American',
  'C.E.O.s' : ' sea E ohs',
  'Jacques' : 'Jock',
  'Cicero' : 'sisser roe',
  'Ehrmantraut' : 'air min trout',
  'Odenkirk' : 'oden kirk',
  'Anime' : 'annie may',
  'Yoknapatawpha' : 'Yok napa tawfa',
  "Baudelaire" : "Bo delair",
  'Ratatouille' : 'rata too E',
  'Siodmak' : 'sea odd mack',
  'Cahiers' : 'ca yey',
  "dramedy" : "drama dee",
  'Georges Sorel' : 'George So rel',
  'Kant' : 'Kont',
  'Bologna' : 'Bolone yuh',
  "dramady" : "drama dee",
  'reminisc' : 'reminiss',
  'montillado' : 'montiyado',
  'Cyrano de Bergerac' : 'Seer a know duh barejairack',
  'Nouvelle Vague' : 'noo vel vahg',
  '(Full Content Review for Parents also available)' : '',
  'Kazan' : 'Kuzaan',
  'fiancée' : 'fiance',
  'von Sydow' : 'von siddo',
  'Ibsen' : 'ibs sen',
  'Elia Kuzaan' : 'eelia kuzaan',
  'Roger Ebert' : 'Roger "E" bert',
  'bons-mot' : 'bone mo',
  'Salome' : 'Sal oh may',
  "s's" : 's',
  'Gwendolen' : 'Gwen dull in',
  '[who?]' : '',
  '.com' : ' dot com',
  'Capt.' : 'Captain',
  '[this quote needs a citation]' : '',
  'sync' : 'sink',
  'Yeats' : 'Yates',
  'Achebe' : 'Ah chay bay',
  'Chinua' : 'chin oo wah',
  'Celtic' : 'Kell tick',
  'fatale' : 'fa\'tall',
  'Geoffery' : 'Jeffry',
  'Guion' : 'Script',
  'Cybill' : 'Sibbul',
  'Teri Garr' : 'Teri Gaar',
  'Leigh' : 'Lee',
  'Cannes' : 'Can',
  'Iran' : 'ear ronn',
  'Robard' : 'Roe Bard',
  'Rhys' : 'Reece',
  "IMAX" : "eye max",
  'paraplegic' : 'para plee jik',
  'Brolin' : 'brole lin',
  'Capote' : 'cup poe tea',
  'Peckinpah' : 'peck in paw',
  'the ID' : 'the id',
  'the Id' : 'the id',
  'Chile' : 'cheelay',
  'BAFTA' : 'bafta',
  'pedophile' : 'peddophile',
  'Washington, D.C.' : 'Washington Dee Sea',
  'Colin ' : 'Call in ',
  'Keitel' : 'kite tell',
  'Wiest' : 'Weest',
  'Coppola' : 'Cope uh luh',
  'Cesar Award' : 'say zar award',
  'Flaubert' : 'Flow bear',
  'ingenue' : 'on gen oo',
  'Charlize' : 'shar lease',
  'pensione' : 'pen see own A',
  'Ruffalo' : 'Rough a low',
  'Spacek' : "spay sick",
  'racecar' : 'race car',
  'Dreiser' : 'Dry zer',
  'Proust' : 'Proost',
  'Henri Bergson' : 'On re bairg sone',
  'Augie' : 'Oggy',
  'Sergio Leone' : 'Sair-Joe Lay-own-E',
  'psychoses' : 'sike oh sieze',
  'chrissake' : 'cry sake',
  'vuitton' : 'voo E tone',
  'Buscemi' : 'Boo shemmy',
  'Quixote' : 'kee ho tay',
  "Groucho" : "grout cho",
  'Werner' : 'Veirner',
  "WASP" : 'wasp',
  "Nighy" : 'Nigh he',
  "Le Carre" : 'Lacar ray',
  'relatable' : 'relate a bull',
  'Ramis' : 'Raymis',
  'codependency' : 'co dependency',
  'protege' : 'protadjay',
  'Roland' : 'Role ind',
  'Rivendell' : 'Riven dell',
  'Elvenking' : 'Elven king',
  'Gyllenhaal' : 'Jill in hall',
  'McConaughey' : 'muck con a hey',
  'Salinger' : 'sal in djer',
  'Metacritic' : 'meta critic',
  "Chabon" : 'Shay bon',
  'Paulo Coelho' : 'paw-lu co-ay-u',
  'Coetzee' : 'koot-zee-uh',
  'Mihaly Csikszentmihalyi' : 'me-high cheek-sent-me-high',
  'JSON' : 'jay sawn',
  'the DOM' : 'the domm',
  'Sigmund' : 'zeeg munt',
  'instantiate' : 'in stan she ate',
  '.js' : ' jay ess',
  'ECMA' : 'E C M "A"',
  'AngularJS' : 'Angular Jay Ess',
  'RESTful' : 'rest full',
  'the UI' : 'the you eye',
  'JavaScript' : 'java script',
  'Luis Bunuel' : 'Lou ees boon you el',
  'Bunuel' : 'boon you el',
  'unmissable' : 'un miss a bull',
  'PEN/Faulkner' : 'Pen, Faulkner',
  'Tomei' : 'Toe May',
  'Stephanides' : 'Steff on a Deez',
  "Washington, D.C." : "Washington D sea",
  'Liotta' : 'Lee oata',
  'Fiennes' : 'Fines',
  'cherubim' : 'shara beam',
  'Benigni' : 'Ben knee knee',
  'S.H.I.E.L.D.' : 'shield',
  'Sacha' : 'sasha',
  'Rylance' : 'rye lince',
  'WWI' : 'World War One',
  'WWII' : 'World War Two',
  'Tucci' : 'toot tchi',
  'Liev Schreiber' : 'Lee yev Schreiber',
  'Saoirse' : 'Seer shaw',
  'Shyamalan' : 'Shama lawn',
  'Malkovich' : 'Malkovitch',
  'Swayze' : 'Sway zee',
  'Pesci' : 'Peshy',
  'Bonham' : 'Bonnum',
  ', Jr.' : ' Junior, ',
  'Jung' : 'Yoong',
  'Huston' : 'Houston',
  'Pynchon' : 'Pinch on',
  'postmodernism' : 'post modernism',
  'Cassel' : 'Cass El',
  'Sr.' : 'Senior',
  'Jr.' : 'Junior',
  'Lt.' : 'Lieutenant',
  'Stephanides' : 'Steff on a deez',
  'Teutonic' : 'two tonic',
  'Halle' : 'Hally',
  'Linklater' : 'Link later',
  'Fritz Lang' : 'Fritz Long',
  'Nazi' : 'not see',
  'Riefenstahl' : 'Reefenschtall',
  'UNESCO' : 'you ness co',
  '[citation needed]' : '',
  '[source needed]' : '',
  'i.e.' : 'in other words',
  'e.g.' : 'for example',
  'LaBeouf' : 'luh buff',
  'rimbaud' : 'rombo',
  '(s)' : 's',
  " 's" : "'s",
  'Federico' : 'Fed air E co',
  'amongst' : 'among', 
  'eschew' : 'eshew',
  'Jacobi' : 'Jack o bee',
  'Uma Thurman' : 'ooma Thurman',
  'Giamatti' : 'gia motti',
  'Phillippe' : 'fulleep',
  'Rev.' : 'Reverend',
  '[edit]' : '; ; ',
  'Jean-Luc Godard' : 'John Luke Go dard',
  'Jonze' : 'Jones',
  'fiancée' : 'fiance',
  'Cotillard' : 'Coat eeyard',
  'Dreyfuss' : 'Dreifus',
  'Eugenides' : 'yujennadeez',
  'Geena' : 'Jeena',
  'Palme d\'Or' : 'palm duh or',
  'Beatty' : 'Batey',
  'Styron' : "Sty run",
  'Tolkien' : 'Tolken',
  'Nazgiul' : 'Naz gull',
  'Gondor' : 'gone door',
  'Balrog' : 'ball rog',
  'Boromir' : 'boro mere',
  'Gamgee' : 'Sam jhee',
  'Saruman' : 'Sarue min',
  'Isildur' : 'eye sull door',
  'Legolas' : 'lego less',
  'Lothloyrien' : 'loth lorry an',
  'Isengard' : 'eye zin guard',
  'Orthanc' : 'or thank',
  'Mordor' : 'more door',
  'Appomattox' : 'Appo maticks',
  'Depardieu' : 'Dup parr diu',
  'Lacan' : 'La con',
  'Georges' : 'George',
  'Daenerys' : 'done heiress',
  'Targaryen' : 'Tar gary in',
  'Khaleesi' : 'call leesi',
  'Tyrion' : 'tearie-un',
  'Viserys' : 'viss heiress',
  'Heinrich Heine' : 'hine rick hine uh',
  'Dieter' : 'Deeter',
  'Cersei' : 'sir say',
  'Drogo' : 'dro go',
  'Berenger' : 'Baron jur',
  'Willem' : 'Will um',
  'Dafoe' : "Dufoe",
  'Benicio' : 'Beneece seeyo',
  'Euripides' : 'your rip id dease',
  'F. Scott' : 'eff scott',
  'Aeschylus' : 'es skull less',
  'Intl.' : 'international',
  'NAACP' : 'N double A C P',
  'their lives' : 'their lyves',
  'our lives' : 'our lyves',
  'the lives' : 'the lyves',
  'many lives' : 'many lyves',
  'Kabul' : 'Cobble',
  'Khaled' : 'Ha led',
  'Hosseini' : 'Ho sane E',
  'Wachowski' : 'Walk cow ski',
  'your lives' : 'your lyves',
  'Nietzschean' : 'neatcha ian',
  'Ayn Rand' : 'I yin Rand',
  'Lt. Col.' : 'Lieutenant colonel',
  'DiCaprio' : 'Decap rio',
  'Poitier' : 'Puwa tea A',
  'DeMille' : 'dumb ill',
  'A. O. Scott' : 'A O Scott',
  'Carell' : 'car L',
  '4.0'  : 'four point oh',
  'Zemeckis' : 'Zemeck iss',
  'J. K. Simmons' : 'jay kay simmons',
  'Les Misérables' : 'lay me zarabla',
  'Les Miserables' : 'lay me zarabla',
  'Kunis' : 'Kooniss',
  'widescreen' : 'wide screen',
  'S/M' : 'ess and em',
  'sadomaso' : 'saidoe maso',
  'Oedipus' : 'Edapus',
  'Oedipal' : 'Edapull',
  'Weisz' : 'Vice',
  'Chrissake' : 'Cry sake',
  'Stradlater' : 'Stradd ladder',
  'crumby' : 'crummy',
  'Josef' : 'Yo zuf',
  'DeLuise' : 'Del lou-ease',
  'crumbier' : 'crummier',
  'Mercutio' : 'mur kiu she oh',
  'Mrs ' : 'Mrs. ',
  'Antolini' : 'antoleenie',
  "Brolin" : "brole lin",
  "Domhnall" : "Dominull",
  'Eilis' : '"A" lish',
  "Ejiofor" : "edgy oh four",
  'Jean-Paul' : 'Jhawn Paul',
  'candide' : 'con deed',
  "Cervantes" : "sair-von tess",
  "Goethe" : 'gurta',
  'Thomas Mann' : 'Toe moss Munn',
  'Saint-Exupery' : 'Sawn Tek Soup parie',
  'Mallarmé' : 'Mall arm may',
  'Stéphane' : 'Steff on',
  "Paglia" : "Palia",
  "Maugham" : "maw um",
  'Prokofiev' : 'prokofe eeyev',
  'Gogol' : 'go goal',
  'entendre' : 'on ton dra',
  "Nyong'o" : "knee on go",
  'Zooey' : 'Zo E',
  'Deschanel' : 'Dayshan El',
  'Corey Haim' : 'Corey Hame',
  'Iwo Jima' : 'E wo jima',
  'Edvard Munch' : 'Ed vard Moonk',
  'Zelig'  : 'zellig',
  'verite' : 'very tay',
  'Guillermo' : 'ghee yermo',
  'Tannhauser' : 'Tahn hoi zer',
  'Tannhäuser' : 'Tahn hoi zer',
  'Preminger' : 'Preming gur',
  'Giacchino' : 'jah kino',
  'Madame' : 'Mad am',
  'Wiig' : 'Wig',
  'Damon' : 'Day min',
  "Pinter" : "Pinnter",
  "9/11" : 'nine eleven',
  'Rogen' : 'Roegen',
  'whilst' : 'while',
  " vs. " : ' versus ',
  'Aykroyd' : 'ack a roid',
  'je ne sais quoi' : 'junna say kwa',
  'Prufrock' : 'proo frock',
  'Cronenberg' : 'Crone in berg',
  'Sartre' : 'Sart truh',
  'Husserl' : 'Huss earl',
  'Michel Foucault' : 'Me shell Foo co',
  'Foucault' : 'Foo co',
  'Vaclav Havel' : 'vat-slav hah-vell',
  'Frankl' : 'Frankel',
  'Wagner' : 'Vahgner',
  'schl' : 'shell',
  'croquet' : 'crow kay',
  'Godot' : 'go doe',
  'camus' : 'cahm moo',
  'Geena' : 'djina',
  'baglady' : 'bag lady',
  'Prospero' : 'Prosper owe',
  'Ovid' : 'Ah vid',
  'Herzog' : 'Hairt sog',
  'Laurent' : 'low ront',
  'Aidan' : '"A" den',
  'fiancé' : 'fiance',
  "exposé" : 'ex poe zay',
  'Onegin' : 'on yeggin',
  'Rimbaud' : 'ram bo',
  "Nietzsche" : 'neatcha',
  '½' : ' and a half',
  "John F. Kennedy": "John F Kennedy",
  'Goldblum' : 'Gold Bloom',
  'Charlize' : 'shar lease',
  'Cazale' : 'Cuzzale',
  'Bette Davis' : 'Betty Davis',
  'John Huston' : 'John Houston',
  'Kerouac' : 'care oh whack',
  'sonuvabitch' : 'son of a bitch',
  'Dickensian' : 'Dick kenzian',
  'Wuddaya' : 'wudda yuh',
  '°F' : ' degrees Fahrenheit',
  'Montaigne' : 'mawn tain',
  'Jamesian' : 'James ian',
  'Thucydides' : 'Thoo sid did dease',
  'fellatio' : 'fellay show',
  'Diderot' : 'Deed a row',
  'Huguenot' : 'Hew gun Oh',
  'Jeunet' : 'Junnay',
  'a.k.a.' : 'ay kay ay',
  'Jean' : 'John',
  'Piaget' : 'pee a jay',
  'verité' : 'very tay',
  'wunderkind' : 'voonder kinned',
  'Chomsky' : 'Tchahmski',
  'Hesse' : 'Hess uh',
  'Hermann' : 'Hair mon',
  '[clarification needed]' : '',
  '/' : ', ',
  '[...]' : ', ',
  '–' : '-',
  '…' : ', ',
  "’" : "'",
  '[' : ', ',
  ']' : ', ',
  "‘" : "'",
  '“' : '"',
  '”' : '"',
  "—" : ', ',
  "…" : ', ',
  'è' : 'e',
  'ł' : 'l',
  'á' : 'a',
  'Á' : 'A',
  'â' : 'a',
  'â' : 'a',
  'Â' : 'A',
  'à' : 'a',
  'À' : 'A',
  'å' : 'a',
  'Å' : 'A',
  'ã' : 'a',
  'Ã' : 'A',
  'ä' : 'a',
  'Ä' : 'A',
  'æ' : 'ae',
  'Æ' : 'ae',
  'ç' : 's',
  'Ç' : 'S',
  'ð' : 'o',
  'Ð' : 'D',
  'é' : 'e',
  'É' : 'E',
  'ê' : 'e',
  'Ê' : 'E',
  'è' : 'e',
  'È' : 'E',
  'ë' : 'e',
  'Ë' : 'E',
  'í' : 'i',
  'Í' : 'I',
  'î' : 'i',
  'Î' : 'I',
  'ì' : 'i',
  'Ì' : 'I',
  'ï' : 'i',
  'Ï' : 'I',
  'ñ' : 'ni',
  'Ñ' : 'N',
  'ó' : 'o',
  'Ó' : 'O',
  'ô' : 'o',
  'Ô' : 'O',
  'ò' : 'o',
  'Ò' : 'o',
  'ø' : 'o',
  'Ø' : 'O',
  'õ' : 'o',
  'Õ' : 'O',
  'ö' : 'o',
  'Ö' : 'O',
  'ß' : 'ss',
  'þ' : 'b',
  'š' : 's',
  'Š' : 'S', 
  'Þ' : 'b',
  'ú' : 'u',
  'Ú' : 'U',
  'û' : 'u',
  'Û' : 'U',
  'ù' : 'u',
  'Ù' : 'U',
  'ü' : 'u',
  'Ü' : 'U',
  'Ō' : 'O',
  'ō' : 'o',
  'ý' : 'y',
  'Ý' : 'Y',
  'ÿ' : 'y',
  'Brontë' : 'Bron tay',
  'Bronte' : 'Bron tay',
  'menage a trois' : 'may nadge a trois',
}

clipboard = '';
f1 = open(filename, 'r')
for line in f1:
    newline = line
    for i, v in searchreplace1.items():
        newline = newline.replace(str(i), str(v))
    for i, v in searchreplace2.items():
        newline = newline.replace(str(i), str(v))
    newline = re.sub('\[\d+\]', '', newline);
    newline = re.sub('Chapter (IX|IV|V?I{0,3})\b', lambda match: "Chapter {0} ".format(replaceRomanNumerals(match.group(1))), newline);
    newline = re.sub('(Act[s]?) (IX|IV|V?I{0,3})(\n|\s|[,.])', lambda match: "{0}".format(match.group(1) + " " + replaceRomanNumerals(match.group(2))) + match.group(3), newline);
    newline = re.sub('Scene (IX|IV|V?I{0,3})\b', lambda match: "Scene {0} ".format(replaceRomanNumerals(match.group(1))), newline);
    newline = re.sub('([A-Z][a-z]+) (IX|IV|V?I{0,3})\b', lambda match: "{0} {1} ".format(match.group(1), replaceRomanNumeralsOrdinal(match.group(2))), newline);  
    newline = re.sub('£(\d+)', r'\1 pounds', newline);
    newline = re.sub('\[note\s[0-9]+\]', '', newline);
    newline = re.sub('\(([0-9][0-9]{0,2})\)', r'', newline); # remove spaces after initials
    newline = re.sub('([A-Z])\.([A-Z])\.', r'\1 \2 ', newline); # remove spaces after initials
    newline = re.sub('([A-Z])\.\s([A-Z])\.\s', r'\1 \2 ', newline); # remove spaces after initials
    newline = re.sub('\$(\d+)\.([0-9])\smillion', r'\1 point \2 million dollars', newline); # remove spaces after initials
    newline = re.sub('(\d+)-(\d+)', r'\1 to \2', newline);
    newline = re.sub('\(i\)','(1),', newline);
    newline = re.sub('\(ii\)','(2),', newline);
    newline = re.sub('\(iii\)','(3),', newline);
    newline = re.sub('\(iv\)','(4),', newline);
    newline = re.sub('\(v\)','(5),', newline);
    newline = re.sub('\(vi\)','(6),', newline);
    newline = re.sub('\(vii\)','(7),', newline);
    newline = re.sub('\(viii\)','(8),', newline);
    newline = re.sub('\(ix\)','(9),', newline);
    newline = re.sub('([A-Z])\.\s', r'\1 ', newline); # remove dot after single capital letter
    #newline = re.sub('([A-Z]\w+)\s\(([A-Z]\w+(\s)?)+\)', r'\1', newline); # gets rid of actor names with first and last name
    newline = re.sub('\n','; ; \n', newline);
    clipboard = clipboard + newline;
f1.close()
sendToClipBoard(clipboard)
