import time
LAST_EXEC_TIME = 0
COOLDOWN = 5 

from flask import Flask, render_template, request, jsonify
import subprocess
import re
import os

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

@app.route("/experiment2")
def experiment2():
    return render_template("experiment2.html")

@app.route("/experiment2_1")
def experiment2_1():
    return render_template("experiment2_1.html")

@app.route("/experiment2_2")
def experiment2_2():
    return render_template("experiment2_2.html")

@app.route("/experiment2_3")
def experiment2_3():
    return render_template("experiment2_3.html")

@app.route("/experiment2_4")
def experiment2_4():
    return render_template("experiment2_4.html")

@app.route("/experiment3")
def experiment3():
    return render_template("experiment3.html")

@app.route("/experiment3_1")
def experiment3_1():
    return render_template("experiment3_1.html")

@app.route("/experiment4")
def experiment4():
    return render_template("experiment4.html")

@app.route("/experiment4_1")
def experiment4_1():
    return render_template("experiment4_1.html")

@app.route("/experiment5")
def experiment5():
    return render_template("experiment5.html")

@app.route("/experiment5_1")
def experiment5_1():
    return render_template("experiment5_1.html")

@app.route("/experiment6")
def experiment6():
    return render_template("experiment6.html")

@app.route("/experiment6_1")
def experiment6_1():
    return render_template("experiment6_1.html")

@app.route("/experiment7")
def experiment7():
    return render_template("experiment7.html")

@app.route("/experiment7_1")
def experiment7_1():
    return render_template("experiment7_1.html")

@app.route("/experiment8")
def experiment8():
    return render_template("experiment8.html")

@app.route("/experiment8_1")
def experiment8_1():
    return render_template("experiment8_1.html")

@app.route("/experiment9")
def experiment9():
    return render_template("experiment9.html")

@app.route("/experiment9_1")
def experiment9_1():
    return render_template("experiment9_1.html")

@app.route("/experiment10")
def experiment10():
    return render_template("experiment10.html")

@app.route("/experiment10_1")
def experiment10_1():
    return render_template("experiment10_1.html")

def normalize(code):
    return [
        l.replace(" ", "").replace("\t", "")
        for l in code.splitlines()
        if l.strip()
    ]

def check_cooldown():
    global LAST_EXEC_TIME
    now = time.time()

    if now - LAST_EXEC_TIME < COOLDOWN:
        remaining = int(COOLDOWN - (now - LAST_EXEC_TIME))
        return False, remaining

    LAST_EXEC_TIME = now
    return True, 0


def run_scilab(code, output_path):
    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}

    // Check if any plot was generated
    if winsid() == [] then
        error("No plot generated");
    end

    xs2png(winsid()(1), "{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""
    subprocess.run(
        ["scilab", "-nw", "-e", scilab],
        check=True,
        timeout=15
    )

def common_runner(code, ref):
    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    output_path = "static/output.png"

    try:
        run_scilab(code, output_path)
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error"})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({"success": True, "image": "/static/output.png"})

def run_scilab_console(code):

    scilab = f"""
try
{code}
catch
    disp(lasterror());
    exit(1);
end
exit;
"""

    result = subprocess.run(
        ["scilab","-nw","-nb","-quit","-e",scilab],
        capture_output=True,
        text=True,
        timeout=15
    )
    output = result.stdout
    output = output.replace('"','')

    return output

@app.route("/run_exp1_1", methods=["POST"])
def run_exp1_1():
    return common_runner(request.form.get("code",""), """
s=poly(0,'s');
t=0:0.05:30;
K=1;
tau=7;
Sys_1=syslin('c',K/(tau*s+1));
Step_G_s=csim('step',t,Sys_1);
plot2d(t,Step_G_s)
title("Step Response of First Order System")
xlabel("Time in Sec.")
ylabel("Output")
""")


@app.route("/run_exp1_2", methods=["POST"])
def run_exp1_2():
    return common_runner(request.form.get("code",""), """
s=poly(0,'s');
t=0:0.05:30;
K=1;
tau=7;
Sys_1=syslin('c',K/(tau*s+1));
Impulse_G_s=csim('impulse',t,Sys_1);
plot2d(t,Impulse_G_s)
title("Impulse Response of First Order System")
xlabel("Time in Sec.")
ylabel("Output")
""")


@app.route("/run_exp1_3", methods=["POST"])
def run_exp1_3():
    return common_runner(request.form.get("code",""), """
s=poly(0,'s');
t=0:0.05:30;
K=1;
tau=7;
Sys_1=syslin('c',K/(tau*s+1));
u=sin(t);
Sin_G_s=csim(u,t,Sys_1);
plot2d(t,Sin_G_s)
title("Sinusoidal Response of First Order System")
xlabel("Time in Sec.")
ylabel("Output")
""")


@app.route("/run_exp1_4", methods=["POST"])
def run_exp1_4():
    return common_runner(request.form.get("code",""), """
s=poly(0,'s');
t=0:0.05:30;
K=1;
tau=7;
Sys_1=syslin('c',K/(tau*s+1));
Ramp=t;
Ramp_G_s=csim(Ramp,t,Sys_1);
plot2d(t,Ramp_G_s)
title("Ramp Response of First Order System")
xlabel("Time in Sec.")
ylabel("Output")
""")


@app.route("/run_exp1_5", methods=["POST"])
def run_exp1_5():
    return common_runner(request.form.get("code",""), """
s = poly(0,'s');
t = 0:0.05:30;
Sys_2 = syslin('c', 1/(s^2 + 7*s + 10));
Step_G_s = csim('step', t, Sys_2);
plot2d(t, Step_G_s);
""")


@app.route("/run_exp1_6", methods=["POST"])
def run_exp1_6():
    return common_runner(request.form.get("code",""), """
s = poly(0,'s');
t = 0:0.05:30;
Sys_2 = syslin('c', 1/(s^2 + 7*s + 10));
Impulse_G_s = csim('impulse', t, Sys_2);
plot2d(t, Impulse_G_s);
""")


@app.route("/run_exp1_7", methods=["POST"])
def run_exp1_7():
    return common_runner(request.form.get("code",""), """
s = poly(0,'s');
t = 0:0.05:30;
Sys_2 = syslin('c', 1/(s^2 + 7*s + 10));
u = sin(t);
Sin_G_s = csim(u, t, Sys_2);
plot2d(t, Sin_G_s);
""")


@app.route("/run_exp1_8", methods=["POST"])
def run_exp1_8():
    return common_runner(request.form.get("code",""), """
s = poly(0,'s');
t = 0:0.05:30;
Sys_2 = syslin('c', 1/(s^2 + 7*s + 10));
Ramp = t;
Ramp_G_s = csim(Ramp, t, Sys_2);
plot2d(t, Ramp_G_s);
""")


@app.route("/run_exp2_1", methods=["POST"])
def run_exp2_1():
    return common_runner(request.form.get("code",""), """
s=%s;
Wn=5;
E_u=0;
t=0:0.001:10;
G_u=syslin('c',Wn^2,s^2+2*E_u*Wn*s+Wn^2);
C_u=csim('step',t,G_u);
plot2d(t,C_u)
""")


@app.route("/run_exp2_2", methods=["POST"])
def run_exp2_2():
    return common_runner(request.form.get("code",""), """
s=%s;
Wn=5;
E_und=0.1;
t=0:0.001:10;
G_u=syslin('c',Wn^2,s^2+2*E_und*Wn*s+Wn^2);
C_u=csim('step',t,G_u);
plot2d(t,C_u)
""")

@app.route("/run_exp2_3", methods=["POST"])
def run_exp2_3():
    return common_runner(request.form.get("code",""), """
s=%s;
Wn=5;
E_o=5;
t=0:0.001:10;
G_o=syslin('c',Wn^2,s^2+2*E_o*Wn*s+Wn^2);
C_o=csim('step',t,G_o);
plot2d(t,C_o)
""")

@app.route("/run_exp2_4", methods=["POST"])
def run_exp2_4():
    return common_runner(request.form.get("code",""), """
s=%s;
Wn=5;
E_c=1;
t=0:0.001:10;
G_c=syslin('c',Wn^2,s^2+2*E_c*Wn*s+Wn^2);
C_c=csim('step',t,G_c);
plot2d(t,C_c)
""")
@app.route("/run_exp3_1", methods=["POST"])
def run_exp3_1():
    return common_runner(request.form.get("code",""), """
s=%s; 
t=0:0.0001:5;

Sys=syslin('c',25,s^2+4*s+25); 
G_s=csim('step',t,Sys);
plot2d(t,G_s);
xgrid();
title("Response of Second Order System","fontsize",1.5);
xlabel("Time in Sec.","fontsize",1);
ylabel("Output","fontsize",1);

D_Pol=Sys.den; 
z=coeff(D_Pol);
Wn=sqrt(z(1,1)); 
zeta=z(1,2)/(2*Wn); 
Wd=Wn*sqrt(1-zeta^2);

Tp=%pi/Wd;
Mp=100*exp((-%pi*zeta)/sqrt(1-zeta^2));
Td=(1+0.7*zeta)/Wn; 
a=atan(sqrt(1-zeta^2)/zeta); 
Tr=(%pi-a)/Wd; 
Tset=4/(zeta*Wn);

Peak_Time="Peak Time = "+string(Tp)+" secs";
Peak_Overshoot="Peak Overshoot = "+string(Mp)+" percent";
Delay_Time="Delay Time = "+string(Td)+" secs";
Rise_Time="Rise Time = "+string(Tr)+" secs";
Settling_Time="Settling Time = "+string(Tset)+" secs";

xstring(3.2,1.4,"Time Domain Specifications");
xstring(3.2,1.25,Peak_Time);
xstring(3.2,1.1,Peak_Overshoot);
xstring(3.2,0.95,Delay_Time);
xstring(3.2,0.8,Rise_Time);
xstring(3.2,0.65,Settling_Time);

""")
@app.route("/run_exp4_1", methods=["POST"])
def run_exp4_1():
    return common_runner(request.form.get("code",""), """
s = poly(0, 's');
t = 0:0.05:30;
Sys = syslin('c', (s^2 + 5*s + 3) / (s^3 + 3*s^2 + 6*s + 1));
plzr(Sys);
""")
@app.route("/run_exp5_1", methods=["POST"])
def run_exp5_1():
    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})
    code = request.form.get("code","")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})
    try:
        output = run_scilab_console(code)
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})
    return jsonify({"output": output})

@app.route("/run_exp6_1", methods=["POST"])
def run_exp6_1():
    return common_runner(request.form.get("code",""), """
s = poly(0, 's');
t = 0:0.05:30;
Sys = syslin('c', 1/(s^3 + 3*s^2 + 6*s + 1));
evans(Sys);
""")

@app.route("/run_exp7_1", methods=["POST"])
def run_exp7_1():
    return common_runner(request.form.get("code",""), """
s = poly(0, 's');
Sys = syslin('c', (s^2 + 5*s + 3) / (s^3 + 3*s^2 + 6*s + 1));
bode(Sys, 0.01, 100)
""")

@app.route("/run_exp8_1", methods=["POST"])
def run_exp8_1():
    return common_runner(request.form.get("code",""), """
T = 10;
L = 100;

omega = logspace(-1, 2, 1000);
s = %i * omega;

den = s .* (T * s + 1);
num = exp(-s * L);

repf = num ./ den;

rad = abs(repf);
theta = atan(imag(repf), real(repf));

polarplot(theta, rad, style=5)
""")

@app.route("/run_exp9_1", methods=["POST"])
def run_exp9_1():
    return common_runner(request.form.get("code",""), """
s = poly(0, 's');
t = 0:0.05:30;
Sys = syslin('c', 1/(s^3 + 3*s^2 + 6*s + 1));
nyquist(Sys)
""")

@app.route("/run_exp10_1", methods=["POST"])
def run_exp10_1():
    return common_runner(request.form.get("code",""), """
s = %s;

Sys = syslin('c', 100/(s^3 + 13*s^2 + 32*s + 20));
disp(Sys);

t = 0:0.01:10;

Sys_o = csim('step', t, Sys);

subplot(2,1,1);
plot(t, Sys_o);
xtitle("Open Loop Response of System", "Time (sec)", "Response");

Kp = 1.8;
Ki = 2;
Kd = 0.344;

Con = Kp + Ki/s + Kd*s;
disp(Con);

Sys_f = syslin('c', (Con*Sys) / (1 + Con*Sys));
disp(Sys_f);

Sys_c = csim('step', t, Sys_f);

subplot(2,1,2);
plot(t, Sys_c);
xtitle("Response with PID Controller", "Time (sec)", "Response");
""")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
