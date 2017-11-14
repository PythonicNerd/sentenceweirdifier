from googletrans import Translator
import random

t = Translator()
#languages = ['af','ak','sq','am','ar','hy','az','eu','be']

#languages = ['af', 'ach', 'ak', 'am', 'ar', 'az', 'be', 'bem', 'bg', 'bh', 'bn', 'br', 'bs', 'ca', 'chr', 'ckb','co', 'crs', 'cs', 'cy', 'da', 'de', 'ee', 'el', 'en', 'eo', 'es', 'es-419', 'et', 'eu', 'fa', 'fi','fo', 'fr', 'fy', 'ga', 'gaa', 'gd', 'gl', 'gn', 'gu', 'ha', 'haw', 'hi', 'hr', 'ht', 'hu', 'hy', 'ia']

"""
id, ig, is, it, iw, ja, jw, ka, kg, kk, km, kn, ko, kri, ku, ky, la,
lg, ln, lo, loz, lt, lua, lv, mfe, mg, mi, mk, ml, mn, mo, mr, ms, mt,
ne, nl, nn, no, nso, ny, nyn, oc, om, or, pa, pcm, pl, ps, pt-BR,
pt-PT, qu, rm, rn, ro, ru, rw, sd, sh, si, sk, sl, sn, so, sq, sr,
sr-ME, st, su, sv, sw, ta, te, tg, th, ti, tk, tl, tn, to, tr, tt,
tum, tw, ug, uk, ur, uz, vi, wo, xh, xx-bork, xx-elmer, xx-hacker,
xx-klingon, xx-pirate, yi, yo, zh-CN, zh-TW, zu]
"""

languages  = ['japanese','afrikaans','arabic','chinese','irish','french','italian','zulu','swahili','turkish','korean','french','icelandic','hindi','greek','german','dutch','czech','russian','hawaiian','polish','thai','spanish','yiddish']


text = input("Enter a sentence: \n> ")
copy = t.translate(text, dest='english')


for i in range(30):
    try:
        print(str(i) + ')')
        copy = t.translate(copy.text, dest=random.choice(languages))
        print(copy.text)
        print('Language: ' + str(copy.src))
        print('In english: ' + t.translate(copy.text, dest='english').text)
        print('\n')
        print('---------------------------------------------------------------')

    except:
        pass


for i in range(10):
    print('\n')
print(t.translate(copy.text, dest='en').text)
