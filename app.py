import time
LAST_EXEC_TIME = 0
COOLDOWN = 5 

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

import os

@app.route("/run_exp1_1", methods=["POST"])
def run_exp1_1():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=poly(0,'s');
t=0:0.05:30;
K=1;
tau=7;
Sys_1=syslin('c',K/(tau*s+1));
Step_G_s=csim('step',t,Sys_1);
plot2d(t,Step_G_s)
title("Step Response of First Order System")
xlabel("Time in Sec.")
ylabel("Response")
""")

    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"

    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""
    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({
        "success": True,
        "image": "/static/output.png"
    })

@app.route("/run_exp1_2", methods=["POST"])
def run_exp1_2():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=poly(0,'s');
t=0:0.05:30;
K=1;
tau=7;
Sys_1=syslin('c',K/(tau*s+1));
Impulse_G_s=csim('impulse',t,Sys_1);
plot2d(t,Impulse_G_s)
title("Impulse Response of First Order System")
xlabel("Time in Sec.")
ylabel("Response")
""")

    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"

    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""

    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({
        "success": True,
        "image": "/static/output.png"
    })

@app.route("/run_exp1_3", methods=["POST"])
def run_exp1_3():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)
    ref = normalize("""
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
ylabel("Response")
""")
    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"

    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""
    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({
        "success": True,
        "image": "/static/output.png"
    })

@app.route("/run_exp1_4", methods=["POST"])
def run_exp1_4():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
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
ylabel("Response")
""")

    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"

    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""
    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({
        "success": True,
        "image": "/static/output.png"
    })

@app.route("/run_exp1_5", methods=["POST"])
def run_exp1_5():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=poly(0,'s');
t=0:0.05:30;
K=1;
Sys_2=syslin('c',K/(s^2+7*s+10));
Step_G_s=csim('step',t,Sys_2);
plot2d(t,Step_G_s)
title("Step Response of Second Order System")
xlabel("Time in Sec.")
ylabel("Response")
""")

    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"

    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""

    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({
        "success": True,
        "image": "/static/output.png"
    })

@app.route("/run_exp1_6", methods=["POST"])
def run_exp1_6():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=poly(0,'s');
t=0:0.05:30;
K=1;
Sys_2=syslin('c',K/(s^2+7*s+10));
Impulse_G_s=csim('impulse',t,Sys_2);
plot2d(t,Impulse_G_s)
title("Impulse Response of Second Order System")
xlabel("Time in Sec.")
ylabel("Response")
""")
    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"

    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""
    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({
        "success": True,
        "image": "/static/output.png"
    })

@app.route("/run_exp1_7", methods=["POST"])
def run_exp1_7():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=poly(0,'s');
t=0:0.05:30;
K=1;
Sys_2=syslin('c',K/(s^2+7*s+10));
u=sin(t);
Sin_G_s=csim(u,t,Sys_2);
plot2d(t,Sin_G_s)
title("Sinusoidal Response of Second Order System")
xlabel("Time in Sec.")
ylabel("Response")
""")

    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"

    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""
    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({
        "success": True,
        "image": "/static/output.png"
    })

@app.route("/run_exp1_8", methods=["POST"])
def run_exp1_8():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=poly(0,'s');
t=0:0.05:30;
K=1;
Sys_2=syslin('c',K/(s^2+7*s+10));
Ramp=t;
Ramp_G_s=csim(Ramp,t,Sys_2);
plot2d(t,Ramp_G_s)
title("Ramp Response of Second Order System")
xlabel("Time in Sec.")
ylabel("Response")
""")
    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"

    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""
    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({
        "success": True,
        "image": "/static/output.png"
    })
@app.route("/run_exp2_1", methods=["POST"])
def run_exp2_1():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=%s;
Wn=5;
E_u=0;
t=0:0.001:10;
G_u=syslin('c',Wn^2,s^2+2*E_u*Wn*s+Wn^2);
C_u=csim('step',t,G_u);
plot2d(t,C_u)
title("Response of Second Order Undamped System")
xlabel("Time in Sec.")
ylabel("Response")
""")

    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"
    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""

    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({"success": True, "image": "/static/output.png"})

@app.route("/run_exp2_2", methods=["POST"])
def run_exp2_2():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=%s;
Wn=5;
E_und=0.1;
t=0:0.001:10;
G_u=syslin('c',Wn^2,s^2+2*E_und*Wn*s+Wn^2);
C_u=csim('step',t,G_u);
plot2d(t,C_u)
title("Response of Second Order Underdamped System")
xlabel("Time in Sec.")
ylabel("Response")
""")

    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"
    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""

    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({"success": True, "image": "/static/output.png"})


@app.route("/run_exp2_3", methods=["POST"])
def run_exp2_3():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=%s;
Wn=5;
E_o=5;
t=0:0.001:10;
G_o=syslin('c',Wn^2,s^2+2*E_o*Wn*s+Wn^2);
C_o=csim('step',t,G_o);
plot2d(t,C_o)
title("Response of Second Order Overdamped System")
xlabel("Time in Sec.")
ylabel("Response")
""")

    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"
    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""
    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({"success": True, "image": "/static/output.png"})

@app.route("/run_exp2_4", methods=["POST"])
def run_exp2_4():

    allowed, wait = check_cooldown()
    if not allowed:
        return jsonify({"error": f"System busy. Please wait {wait} seconds."})

    code = request.form.get("code", "")
    if not code.strip():
        return jsonify({"error": "Program cannot be empty."})

    student_norm = normalize(code)

    ref = normalize("""
s=%s;
Wn=5;
E_c=1;
t=0:0.001:10;
G_c=syslin('c',Wn^2,s^2+2*E_c*Wn*s+Wn^2);
C_c=csim('step',t,G_c);
plot2d(t,C_c)
title("Response of Second Order Critically damped System")
xlabel("Time in Sec.")
ylabel("Response")
""")

    if student_norm == ref:
        return jsonify({"error": "Reference program should not be copied exactly."})

    output_path = "static/output.png"
    if os.path.exists(output_path):
        os.remove(output_path)

    scilab = f"""
try
    {code}
    xs2png(0,"{output_path}");
catch
    disp(lasterror());
    exit(1);
end
exit;
"""
    try:
        subprocess.run(
            ["scilab", "-nw", "-e", scilab],
            check=True,
            timeout=15
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Scilab execution error. Check your syntax."})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out."})

    if not os.path.exists(output_path):
        return jsonify({"error": "No output generated. Please check your program."})

    return jsonify({"success": True, "image": "/static/output.png"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
