from androguard.core.bytecodes.apk import APK
from .risk_matrix import PERM_RISK_MAP

def analyze(apk_path:str)->dict:
    apk = APK(apk_path)
    perms = apk.get_permissions()
    out, total = [],0
    for p in perms:
        risk = PERM_RISK_MAP.get(p,1)
        out.append({"name":p,"risk":risk})
        total += risk
    avg = round(total/len(out),2) if out else 0
    return {"permissions":sorted(out,key=lambda x:x["risk"],reverse=True),"score":avg}
