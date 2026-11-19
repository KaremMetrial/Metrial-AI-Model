# per-investigation LLM cost
def llm(pin_h,pout_h,pin_s,pout_s,cache_read=0.1):
    # tokens in thousands
    triage = 20*pin_h/1000 + 2*pout_h/1000           # Haiku, $ (tokens k * $/M /1000)
    # sonnet: 60k in, 70% cache-read, 30% fresh, 1 cache write of 20k at 1.25x; 6k out
    inv = (60*0.3*pin_s + 60*0.7*cache_read*pin_s + 20*0.25*pin_s*0.0 + 6*pout_s)/1000
    ver = (15*pin_s + 2*pout_s)/1000
    return triage+inv+ver
for name,p in {'cons(Sonnet4.6 3/15,Haiku 1/5)':(1,5,3,15),'base(Sonnet5.5 2/10)':(1,5,2,10),'opt(batch -50% base)':(.5,2.5,1,5)}.items():
    c=llm(*p); print(name, round(c,3),'per investigation')
sc={'cons':dict(price=450,inv=80,llm=0.45,infra=60,ingest=40,val_h=0.5,cs=1/25,churn=.025),
    'base':dict(price=900,inv=60,llm=0.30,infra=45,ingest=30,val_h=0.3,cs=1/40,churn=.015),
    'opt':dict(price=1500,inv=50,llm=0.15,infra=35,ingest=25,val_h=0.15,cs=1/60,churn=.01)}
head={5:2,20:3,100:8,500:28}
fixed_tools={5:1500,20:2500,100:8000,500:30000} # soc2, observability, tooling, legal, cloud base
for s,a in sc.items():
  for n in (5,20,100,500):
    rev=n*a['price']
    llmc=n*a['inv']*a['llm']
    infra=n*(a['infra']+a['ingest'])
    val=n*a['inv']*a['val_h']*0.25*55/ (1)   # 25% of investigations human-reviewed, $55/h loaded
    val=n*a['val_h']*55*4   # hours/customer/month = val_h*4 reviewed batches (simplify)
    cs=n*a['cs']*10000
    cogs=llmc+infra+val+cs
    gm=rev-cogs
    people=head[n]*12000
    opex=people+fixed_tools[n]
    op=gm-opex
    print(f"{s:4}{n:4} rev{rev:9.0f} cogs{cogs:9.0f} GM{gm/rev*100:5.1f}% opex{opex:9.0f} op{op:9.0f} llm{llmc:7.0f} infra{infra:7.0f} val{val:7.0f} cs{cs:7.0f}")
  # breakeven customers
  for n in range(1,3000):
    h=2 if n<12 else 3 if n<40 else 8 if n<250 else 28
    rev=n*a['price'];c=n*(a['inv']*a['llm']+a['infra']+a['ingest']+a['val_h']*220+a['cs']*10000)
    if rev-c-h*12000-(1500 if n<12 else 2500 if n<40 else 8000 if n<250 else 30000)>0: print(' breakeven',s,n);break
# team sustain: 3 people at 8k loaded=24k+3k tools => need GP 27k
for a_ in ('cons','base','opt'):
  a=sc[a_]; unit=a['price']-(a['inv']*a['llm']+a['infra']+a['ingest']+a['val_h']*220+a['cs']*10000)
  print(a_,'unit contrib',round(unit),'cust for 27k',round(27000/unit,1),'cust for 2-person 18k',round(18000/unit,1))
