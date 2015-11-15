#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from AppKit import NSPasteboard,NSObject,NSStringPboardType

def sendToClipBoard(string):
    pasteboard = NSPasteboard.generalPasteboard()
    emptyOwner = NSObject.alloc().init()
    pasteboard.declareTypes_owner_([NSStringPboardType], emptyOwner)
    pasteboard.setString_forType_(string, NSStringPboardType)


filename = '/Users/oknate2/Downloads/sample.txt'

searchreplace  = {
  'née' : 'nay',
  'Fiennes' : 'Fines',
  'Ralph Fines' : 'Rafe Fines',
  'Scorsese' : 'Score Sazie',
  'Anthony Hopkins' : 'Ann tonnie Hopkins',
  'Nolte': 'noltee',
  'Baruchel' : 'Baroo shell',
  'Rene Descartes' : 'rennay day cart',
  'Descartes' : 'day cart',
  'Theroux' : 'Thero',
  'Warner Bros.' : 'Warner Brothers',
  'Galifianakis' : 'gall lif fee a nakis',
  'Mathieu' : 'Matt hew',
  'Haneke' : 'Haneka',
  'Truffaut' : 'True foe',
  'lives' : 'livs',
  'the livs' : 'the lives',
  'Von Trier' : 'von treer',
  'von Trier' : 'von treer',
  'Jean Genet' : 'John \'ngine nay',
  'Genet' : '\'ngine nay',
  'Friedrich' : 'free drish',
  'Dürrenmatt' : 'durenmott',
  'Arrabal' : 'Ah rah ball',
  'Havel' : 'Hov vell',
  'Albert Camus' : 'All bear come mu',
  'Jodorowsky' : 'hoder off ski',
  'phoneticist' : 'phonetisist',
  'cliché' : 'klee shay',
  "bipolarity" : "by polarity",
  "oxymoronic" : 'ocksie moronic',
  "Gena Rowlands" : "Jeana Rowlands",
  'Iñárritu' : 'eenya re two',
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
  "dramady" : "drama dee",
  'reminisc' : 'reminiss',
  'montillado' : 'montiyado',
  ' does' : ' duz',
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
  'Chile' : 'cheel lay',
  'BAFTA' : 'bafta',
  'pedophile' : 'peddophile',
  'Washington, D.C.' : 'Washington Dee Sea',
  'Colin ' : 'Call in ',
  'Keitel' : 'kite tell',
  'Wiest' : 'Weest',
  'Coppola' : 'Cope uh luh',
  'Cesar Award' : 'say zar award',
  'Gustave Flaubert' : 'Goo staav Flow bear',
  'ingenue' : 'on gen oo',
  'Charlize' : 'shar lease',
  'pensione' : 'pen see own A',
  'Ruffalo' : 'Rough a low',
  'Spacek' : "spay sick",
  'racecar' : 'race car',
  'Dreiser' : 'Dry zer',
  'Proust' : 'Proost',
  'Augie' : 'Oggy',
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
  'Saoirse' : 'Seer shaw',
  'Shyamalan' : 'Shama lawn',
  'Malkovich' : 'Malkovitch',
  'Swayze' : 'Sway zee',
  'Pesci' : 'Peshy',
  'Bonham' : 'Bonnum',
  ', Jr.' : ' Junior',
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
  'U.S.' : 'US',
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
  'Beatty': 'Batey',
  'Depardieu' : 'Duh pardyu',
  'Lacan' : 'La con',
  'Berenger' : 'Baron jur',
  'Willem' : 'Will um',
  'Dafoe' : "Dufoe",
  'Benicio' : 'Ben knee siyo',
  'Euripides' : 'your rip id dease',
  'F. Scott' : 'eff scott',
  'Aeschylus' : 'es skull less',
  'Intl.' : 'international',
  'Nietzschean' : 'neat chee in',
  'Ayn Rand' : 'I yin Rand',
  'DiCaprio' : 'Duh Cap preeyo',
  'DeMille' : 'damill',
  'A. O. Scott' : 'A O Scott',
  'Carell' : 'car L',
  '4.0'  : 'four point oh',
  'Zemeckis' : 'Zemeck iss',
  'J. K. Simmons' : 'jay kay simmons',
  'Wachowski' : 'whack cow ski',
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
  'crumbier' : 'crummier',
  'Mercutio' : 'mur kiu she oh',
  'Antolini' : 'antoleenie',
  "Brolin" : "brole in",
  "Ejiofor" : "edgy oh four",
  "Cervantes" : "sir van tease",
  "Goethe" : 'gurta',
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
  "Pinter" : "Pinnter",
  "9/11" : 'nine eleven',
  'Rogen' : 'Roegen',
  'whilst' : 'while',
  "vs. " : 'versus ',
  'Aykroyd' : 'ack a roid',
  'je ne sais quoi' : 'junna say kwa',
  'Prufrock' : 'proo frock',
  'Cronenberg' : 'Crone in berg',
  'naïve' : 'naive',
  'Sartre' : 'Sart truh',
  'Wagner' : 'Vogner',
  'croquet' : 'crow kay',
  'Godot' : 'go doe',
  'camus' : 'kam moo',
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
  "Nietzsche" : 'neat cha',
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
  'Jamesian' : 'James ian',
  'fellatio' : 'fellay show',
  'Jeunet' : 'Junnay',
  'mores' : ' moraze',
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
  'Þ' : 'b',
  'ú' : 'u',
  'Ú' : 'U',
  'û' : 'u',
  'Û' : 'U',
  'ù' : 'u',
  'Ù' : 'U',
  'ü' : 'u',
  'Ü' : 'U',
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
    for i, v in searchreplace.items():
        newline = newline.replace(str(i), str(v))
    newline = re.sub('\[\d+\]', '', newline);
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