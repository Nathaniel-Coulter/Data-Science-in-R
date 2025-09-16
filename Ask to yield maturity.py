import os
import math
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

csv_path = r"C:\Users\ncoul778\Downloads\BB-Treasuries.csv"

SETTLEMENT_STR = None  # EX "2025-09-16"

def parse_date(s):

    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d-%b-%Y", "%b %d, %Y"):
        try:
            return datetime.strptime(str(s), fmt).date()
        except Exception:
            pass

    try:
        return pd.to_datetime(s).date()
    except Exception:
        return None

def to_decimal_rate(x):
    """Convert a coupon or yield to decimal. If it's >= 1.0 we treat as percent (e.g. 4.25 -> 0.0425)."""
    try:
        v = float(x)
    except Exception:
        return None
    return v / 100.0 if v >= 1.0 else v

def generate_coupon_dates(maturity, freq=2, back_until=None):
    """Return a list of coupon dates going backward from maturity by freq until back_until (exclusive)."""
    step = 12 // freq
    dates = [maturity]

    for _ in range(200):
        nxt = dates[-1] - relativedelta(months=step)
        dates.append(nxt)
        if back_until and nxt <= back_until - relativedelta(days=366*50):  
            break
        if back_until and nxt <= back_until - relativedelta(months=24*step):
           
            pass
        if nxt.year < 1900:  
            break
    return sorted(d for d in dates)

def price_clean_from_ytm(coupon_rate, maturity_date, ytm, settle_date, freq=2):
    """
    Street-style bond pricing for Treasuries:
    - Semiannual coupons (freq=2)
    - Actual/Actual day count for accrual fraction
    - Clean price = Full price - Accrued
    All prices per 100 par.
    """
    if settle_date >= maturity_date:
        return float('nan')


    sched = generate_coupon_dates(maturity_date, freq=freq)

    last = None
    next_ = None
    for i in range(1, len(sched)):
        if sched[i-1] <= settle_date < sched[i]:
            last = sched[i-1]
            next_ = sched[i]
            break
    if last is None or next_ is None:

        sched_sorted = sorted(sched)
        next_ = min([d for d in sched_sorted if d > settle_date], default=None)
        last = max([d for d in sched_sorted if d <= settle_date], default=None)
        if last is None or next_ is None:
            return float('nan')


    days_in_period = (next_ - last).days
    days_since_last = (settle_date - last).days
    if days_in_period <= 0:
        return float('nan')
    alpha = days_since_last / days_in_period  



    remaining_dates = [d for d in sched if d > settle_date]

    N = len(remaining_dates)

    m = freq
    c = coupon_rate  
    y = ytm          

    coup = 100 * c / m
    per = 1.0 + y / m



    full = 0.0
    for k in range(1, N + 1):
        cf = coup
        if k == N:
            cf += 100.0
        full += cf / (per ** (k - alpha))


    accrued = coup * alpha

    clean = full - accrued
    return clean


df = pd.read_csv(csv_path)


settle = date.today() if SETTLEMENT_STR is None else datetime.strptime(SETTLEMENT_STR, "%Y-%m-%d").date()


COL_COUPON = "Coupon"
COL_MATURITY = "Maturity"
COL_ASK_YTM = "Ask Yield to Maturity"
COL_ASK_PX  = "Ask Price"  


coupons = df[COL_COUPON].apply(to_decimal_rate)          
maturities = df[COL_MATURITY].apply(parse_date)
ask_ytms = df[COL_ASK_YTM].apply(to_decimal_rate)        


prices = []
for c, mdt, y in zip(coupons, maturities, ask_ytms):
    if c is None or mdt is None or y is None:
        prices.append(float('nan'))
        continue
    prices.append(price_clean_from_ytm(c, mdt, y, settle, freq=2))

df["Ask_Price_From_YTM"] = prices


if COL_ASK_PX in df.columns:
    try:
        df["Ask_Diff"] = df["Ask_Price_From_YTM"] - df[COL_ASK_PX]
    except Exception:
        pass


base, ext = os.path.splitext(csv_path)
out_path = base + "_repriced_from_ytm" + ext
df.to_csv(out_path, index=False)


print(f"Settlement date used: {settle.isoformat()}")
cols_to_show = ["Name", "Ticker", COL_COUPON, COL_MATURITY, COL_ASK_YTM, "Ask_Price_From_YTM"]
if COL_ASK_PX in df.columns:
    cols_to_show.append(COL_ASK_PX)
    if "Ask_Diff" in df.columns:
        cols_to_show.append("Ask_Diff")
print(df[cols_to_show].head(12))
print(f"\nSaved to: {out_path}")
