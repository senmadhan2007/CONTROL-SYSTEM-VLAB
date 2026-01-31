from flask import Flask, render_template, request, jsonify
import subprocess
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/experiment1")
def experiment1():
    return render_template("experiment1.html")

@app.route("/experiment1_1")
def experiment1_1():
    return render_template("experiment1_1.html")

@app.route("/experiment1_2")
def experiment1_2():
    return render_template("experiment1_2.html")

@app.route("/experiment1_3")
def experiment1_3():
    return render_template("experiment1_3.html")

@app.route("/experiment1_4")
def experiment1_4():
    return render_template("experiment1_4.html")

@app.route("/experiment1_5")
def experiment1_5():
    return render_template("experiment1_5.html")

@app.route("/experiment1_6")
def experiment1_6():
    return render_template("experiment1_6.html")

@app.route("/experiment1_7")
def experiment1_7():
    return render_template("experiment1_7.html")

@app.route("/experiment1_8")
def experiment1_8():
    return render_template("experiment1_8.html")

def normalize(code):
    return [
        l.replace(" ", "").replace("\t", "")
        for l in code.splitlines()
        if l.strip()
    ]

@app.route("/run_exp1_1", methods=["POST"])
def run_exp1_1():
    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    lines = normalize(code)
    normalized = []
    K = None
    tau = None

    for line in lines:
        m = re.match(
            r"Sys_1=syslin\('c',([\d.]+)/\(([\d.]+)\*s\+1\)\);?",
            line
        )
        if m:
            K = m.group(1)
            tau = m.group(2)
            line = "Sys_1=syslin('c',K/(τ*s+1));"
        normalized.append(line)

    ref = normalize("""
        s=poly(0,'s');
        t=0:0.05:30;
        Sys_1=syslin('c',K/(τ*s+1));
        Step_G_s=csim('step',t,Sys_1);
        plot2d(t,Step_G_s);
        title("StepResponseofFirstOrderSystem");
        xlabel("TimeinSec.");
        ylabel("Response");
    """)

    if K is None or tau is None or normalized != ref:
        return jsonify({"error": "Only numerator (K) and time constant (τ) may be changed."})

    scilab = f"""
    s=poly(0,'s');
    t=0:0.05:30;
    Sys_1=syslin('c',{K}/({tau}*s+1));
    Step_G_s=csim('step',t,Sys_1);
    plot2d(t,Step_G_s);
    title("Step Response of First Order System");
    xlabel("Time in Sec.");
    ylabel("Response");
    xs2png(0,"static/output.png");
    exit;
    """
    subprocess.run(["scilab", "-nw", "-e", scilab], check=True)
    return jsonify({"success": True})

@app.route("/run_exp1_2", methods=["POST"])
def run_exp1_2():
    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    lines = normalize(code)
    normalized = []
    K = None
    tau = None

    for line in lines:
        m = re.match(
            r"Sys_1=syslin\('c',([\d.]+)/\(([\d.]+)\*s\+1\)\);?",
            line
        )
        if m:
            K = m.group(1)
            tau = m.group(2)
            line = "Sys_1=syslin('c',K/(τ*s+1));"
        normalized.append(line)

    ref = normalize("""
        s=poly(0,'s');
        t=0:0.05:30;
        Sys_1=syslin('c',K/(τ*s+1));
        Impulse_G_s=csim('impulse',t,Sys_1);
        plot2d(t,Impulse_G_s);
        title("ImpulseResponseofFirstOrderSystem");
        xlabel("TimeinSec.");
        ylabel("Response");
    """)

    if K is None or tau is None or normalized != ref:
        return jsonify({"error": "Only numerator (K) and time constant (τ) may be changed."})

    scilab = f"""
    s=poly(0,'s');
    t=0:0.05:30;
    Sys_1=syslin('c',{K}/({tau}*s+1));
    Impulse_G_s=csim('impulse',t,Sys_1);
    plot2d(t,Impulse_G_s);
    title("Impulse Response of First Order System");
    xlabel("Time in Sec.");
    ylabel("Response");
    xs2png(0,"static/output.png");
    exit;
    """
    subprocess.run(["scilab", "-nw", "-e", scilab], check=True)
    return jsonify({"success": True})

@app.route("/run_exp1_3", methods=["POST"])
def run_exp1_3():
    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    lines = normalize(code)
    normalized = []
    K = None
    tau = None

    for line in lines:
        m = re.match(
            r"Sys_1=syslin\('c',([\d.]+)/\(([\d.]+)\*s\+1\)\);?",
            line
        )
        if m:
            K = m.group(1)
            tau = m.group(2)
            line = "Sys_1=syslin('c',K/(τ*s+1));"
        normalized.append(line)

    ref = normalize("""
        s=poly(0,'s');
        t=0:0.05:30;
        Sys_1=syslin('c',K/(τ*s+1));
        u=sin(t);
        Sin_G_s=csim(u,t,Sys_1);
        plot2d(t,Sin_G_s);
        title("SinusoidalResponseofFirstOrderSystem");
        xlabel("TimeinSec.");
        ylabel("Response");
    """)

    if K is None or tau is None or normalized != ref:
        return jsonify({"error": "Only numerator (K) and time constant (τ) may be changed."})

    scilab = f"""
    s=poly(0,'s');
    t=0:0.05:30;
    Sys_1=syslin('c',{K}/({tau}*s+1));
    u=sin(t);
    Sin_G_s=csim(u,t,Sys_1);
    plot2d(t,Sin_G_s);
    title("Sinusoidal Response of First Order System");
    xlabel("Time in Sec.");
    ylabel("Response");
    xs2png(0,"static/output.png");
    exit;
    """
    subprocess.run(["scilab", "-nw", "-e", scilab], check=True)
    return jsonify({"success": True})

@app.route("/run_exp1_4", methods=["POST"])
def run_exp1_4():
    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    lines = normalize(code)
    normalized = []
    K = None
    tau = None

    for line in lines:
        m = re.match(
            r"Sys_1=syslin\('c',([\d.]+)/\(([\d.]+)\*s\+1\)\);?",
            line
        )
        if m:
            K = m.group(1)
            tau = m.group(2)
            line = "Sys_1=syslin('c',K/(τ*s+1));"
        normalized.append(line)

    ref = normalize("""
        s=poly(0,'s');
        t=0:0.05:30;
        Sys_1=syslin('c',K/(τ*s+1));
        Ramp=t;
        Ramp_G_s=csim(Ramp,t,Sys_1);
        plot2d(t,Ramp_G_s);
        title("RampResponseofFirstOrderSystem");
        xlabel("TimeinSec.");
        ylabel("Response");
    """)

    if K is None or tau is None or normalized != ref:
        return jsonify({"error": "Only numerator (K) and time constant (τ) may be changed."})

    scilab = f"""
    s=poly(0,'s');
    t=0:0.05:30;
    Sys_1=syslin('c',{K}/({tau}*s+1));
    Ramp=t;
    Ramp_G_s=csim(Ramp,t,Sys_1);
    plot2d(t,Ramp_G_s);
    title("Ramp Response of First Order System");
    xlabel("Time in Sec.");
    ylabel("Response");
    xs2png(0,"static/output.png");
    exit;
    """
    subprocess.run(["scilab", "-nw", "-e", scilab], check=True)
    return jsonify({"success": True})

@app.route("/run_exp1_5", methods=["POST"])
def run_exp1_5():
    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    lines = normalize(code)
    normalized = []
    K = None

    for line in lines:
        m = re.match(
            r"Sys_2=syslin\('c',([\d.]+)/\(s\^2\+7\*s\+10\)\);?",
            line
        )
        if m:
            K = m.group(1)
            line = "Sys_2=syslin('c',K/(s^2+7*s+10));"
        normalized.append(line)

    ref = normalize("""
        s=poly(0,'s');
        t=0:0.05:30;
        Sys_2=syslin('c',K/(s^2+7*s+10));
        Step_G_s=csim('step',t,Sys_2);
        plot2d(t,Step_G_s);
        title("StepResponseofSecondOrderSystem");
        xlabel("TimeinSec.");
        ylabel("Response");
    """)

    if K is None or normalized != ref:
        return jsonify({"error": "Only numerator (K) may be changed."})

    scilab = f"""
    s=poly(0,'s');
    t=0:0.05:30;
    Sys_2=syslin('c',{K}/(s^2+7*s+10));
    Step_G_s=csim('step',t,Sys_2);
    plot2d(t,Step_G_s);
    title("Step Response of Second Order System");
    xlabel("Time in Sec.");
    ylabel("Response");
    xs2png(0,"static/output.png");
    exit;
    """
    subprocess.run(["scilab", "-nw", "-e", scilab], check=True)
    return jsonify({"success": True})

@app.route("/run_exp1_6", methods=["POST"])
def run_exp1_6():
    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    lines = normalize(code)
    normalized = []
    K = None

    for line in lines:
        m = re.match(
            r"Sys_2=syslin\('c',([\d.]+)/\(s\^2\+7\*s\+10\)\);?",
            line
        )
        if m:
            K = m.group(1)
            line = "Sys_2=syslin('c',K/(s^2+7*s+10));"
        normalized.append(line)

    ref = normalize("""
        s=poly(0,'s');
        t=0:0.05:30;
        Sys_2=syslin('c',K/(s^2+7*s+10));
        Impulse_G_s = csim('impulse', t, Sys_2);
        plot2d(t,Impulse_G_s);
        title("Impulse Response of Second Order System");
        xlabel("TimeinSec.");
        ylabel("Response");
    """)

    if K is None or normalized != ref:
        return jsonify({"error": "Only numerator (K) may be changed."})

    scilab = f"""
    s=poly(0,'s');
    t=0:0.05:30;
    Sys_2=syslin('c',{K}/(s^2+7*s+10));
    Impulse_G_s = csim('impulse', t, Sys_2);
    plot2d(t,Impulse_G_s);
    title("Impulse Response of Second Order System");
    xlabel("Time in Sec.");
    ylabel("Response");
    xs2png(0,"static/output.png");
    exit;
    """
    subprocess.run(["scilab", "-nw", "-e", scilab], check=True)
    return jsonify({"success": True})

@app.route("/run_exp1_7", methods=["POST"])
def run_exp1_7():
    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    lines = normalize(code)
    normalized = []
    K = None

    for line in lines:
        m = re.match(
            r"Sys_2=syslin\('c',([\d.]+)/\(s\^2\+7\*s\+10\)\);?",
            line
        )
        if m:
            K = m.group(1)
            line = "Sys_2=syslin('c',K/(s^2+7*s+10));"
        normalized.append(line)

    ref = normalize("""
        s=poly(0,'s');
        t=0:0.05:30;
        Sys_2=syslin('c',K/(s^2+7*s+10));
        u=sin(t);
        Sin_G_s=csim(u,t,Sys_2);
        plot2d(t,Sin_G_s);
        title("SinusoidalResponseofSecondOrderSystem");
        xlabel("TimeinSec.");
        ylabel("Response");
    """)

    if K is None or normalized != ref:
        return jsonify({"error": "Only numerator (K) may be changed."})

    scilab = f"""
    s=poly(0,'s');
    t=0:0.05:30;
    Sys_2=syslin('c',{K}/(s^2+7*s+10));
    u=sin(t);
    Sin_G_s=csim(u,t,Sys_2);
    plot2d(t,Sin_G_s);
    title("Sinusoidal Response of Second Order System");
    xlabel("Time in Sec.");
    ylabel("Response");
    xs2png(0,"static/output.png");
    exit;
    """

    subprocess.run(["scilab", "-nw", "-e", scilab], check=True)
    return jsonify({"success": True})

@app.route("/run_exp1_8", methods=["POST"])
def run_exp1_8():
    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    lines = normalize(code)
    normalized = []
    K = None

    for line in lines:
        # Match: Sys_2=syslin('c',K/(s^2+7*s+10));
        m = re.match(
            r"Sys_2=syslin\('c',([\d.]+)/\(s\^2\+7\*s\+10\)\);?",
            line
        )
        if m:
            K = m.group(1)
            line = "Sys_2=syslin('c',K/(s^2+7*s+10));"
        normalized.append(line)

    ref = normalize("""
        s=poly(0,'s');
        t=0:0.05:30;
        Sys_2=syslin('c',K/(s^2+7*s+10));
        Ramp=t;
        Ramp_G_s=csim(Ramp,t,Sys_2);
        plot2d(t,Ramp_G_s);
        title("RampResponseofSecondOrderSystem");
        xlabel("TimeinSec.");
        ylabel("Response");
    """)

    if K is None or normalized != ref:
        return jsonify({"error": "Only numerator (K) may be changed."})

    scilab = f"""
    s=poly(0,'s');
    t=0:0.05:30;
    Sys_2=syslin('c',{K}/(s^2+7*s+10));
    Ramp=t;
    Ramp_G_s=csim(Ramp,t,Sys_2);
    plot2d(t,Ramp_G_s);
    title("Ramp Response of Second Order System");
    xlabel("Time in Sec.");
    ylabel("Response");
    xs2png(0,"static/output.png");
    exit;
    """

    subprocess.run(["scilab", "-nw", "-e", scilab], check=True)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
