const questions = [
{
question:"A control system in which the control action is independent of the output is called",
options:["Closed loop system","Feedback system","Open loop system","Automatic system"],
answer:2
},

{
question:"A system that uses feedback to control its output is known as",
options:["Open loop system","Closed loop system","Linear system","Time invariant system"],
answer:1
},

{
question:"The transfer function of a system is defined as",
options:["Output/Input in time domain","Input/Output in Laplace domain","Output/Input in Laplace domain","Time constant"],
answer:2
},

{
question:"Transfer function is applicable only when the system is",
options:["Linear and time invariant","Nonlinear","Time varying","Dynamic"],
answer:0
},

{
question:"The Laplace transform of the transfer function assumes",
options:["Zero initial conditions","Non-zero initial conditions","Infinite initial conditions","Random conditions"],
answer:0
},

{
question:"Which system improves accuracy and reduces error?",
options:["Open loop system","Closed loop system","Static system","Manual system"],
answer:1
},

{
question:"In a feedback control system, the feedback element is used to",
options:["Amplify signal","Compare output with input","Generate reference signal","Increase gain"],
answer:1
},

{
question:"Which of the following is an example of an open loop control system?",
options:["Temperature controller","Automatic washing machine","Electric toaster","Speed governor"],
answer:2
},

{
question:"Which of the following is an example of a closed loop control system?",
options:["Electric heater","Water level controller","Traffic light timer","Electric kettle"],
answer:1
},

{
question:"The transfer function of a system depends on",
options:["System structure","System parameters","Initial conditions","System parameters only"],
answer:1
},

{
question:"Block diagram representation is used to",
options:["Simplify complex control systems","Increase gain","Reduce noise","Increase stability"],
answer:0
},

{
question:"In block diagram representation, the arrow indicates",
options:["Signal direction","Gain","Transfer function","Noise"],
answer:0
},

{
question:"A block in block diagram represents",
options:["Mathematical operation","Transfer function","Physical component","Controller"],
answer:1
},

{
question:"Signal flow graph technique was developed by",
options:["Mason","Nyquist","Routh","Bode"],
answer:0
},

{
question:"The formula used in signal flow graph analysis is",
options:["Nyquist formula","Mason's gain formula","Bode equation","Hurwitz equation"],
answer:1
},

{
question:"In signal flow graph, nodes represent",
options:["System gain","System variables","Transfer function","Input signal"],
answer:1
},

{
question:"A path from input node to output node without repeating nodes is called",
options:["Loop","Forward path","Node path","Gain path"],
answer:1
},

{
question:"A closed path in signal flow graph is known as",
options:["Loop","Branch","Node","Path"],
answer:0
},

{
question:"Non touching loops are loops that",
options:["Have same gain","Do not share common nodes","Are negative","Are positive"],
answer:1
},

{
question:"Mechanical translational system uses which physical variables?",
options:["Voltage and current","Force and velocity","Pressure and flow","Temperature and heat"],
answer:1
},

{
question:"Mechanical rotational systems use",
options:["Torque and angular displacement","Voltage and current","Force and velocity","Pressure and flow"],
answer:0
},

{
question:"Mass in mechanical system is analogous to",
options:["Inductor","Capacitor","Resistor","Transformer"],
answer:0
},

{
question:"Spring constant in mechanical system corresponds to",
options:["Inductance","Capacitance","Resistance","Voltage"],
answer:1
},

{
question:"Damper in mechanical system corresponds to",
options:["Resistor","Capacitor","Inductor","Diode"],
answer:0
},

{
question:"Which law is commonly used to model electrical systems?",
options:["Newton's law","Kirchhoff's laws","Coulomb's law","Faraday's law"],
answer:1
},

{
question:"The number of poles of a transfer function indicates",
options:["System order","Gain","Stability","Input type"],
answer:0
},

{
question:"The denominator of transfer function represents",
options:["Input","Characteristic equation","Output","Gain"],
answer:1
},

{
question:"The numerator of transfer function represents",
options:["System dynamics","Zeros of system","Poles of system","Time constant"],
answer:1
},

{
question:"A system is said to be causal if",
options:["Output depends on future input","Output depends on present and past input","Output independent of input","Output constant"],
answer:1
},

{
question:"Block diagram reduction helps to",
options:["Increase system gain","Obtain overall transfer function","Increase stability","Reduce noise"],
answer:1
},

{
question:"The transfer function of a first-order system is generally written as",
options:["K/s","K/(τs+1)","1/s²","K/(s²+s+1)"],
answer:1
},

{
question:"The parameter τ in a first-order system represents",
options:["Gain","Damping ratio","Time constant","Natural frequency"],
answer:2
},

{
question:"The response of a system immediately after input is applied is called",
options:["Steady state response","Transient response","Frequency response","Static response"],
answer:1
},

{
question:"The response of a system after a long time is called",
options:["Transient response","Dynamic response","Steady state response","Initial response"],
answer:2
},

{
question:"The input commonly used to study time response is",
options:["Step input","Impulse input","Ramp input","All of the above"],
answer:3
},

{
question:"For a first-order system, the output reaches 63.2% of its final value at",
options:["2τ","τ","3τ","4τ"],
answer:1
},

{
question:"The general transfer function of a second-order system is",
options:["K/(s+1)","K/(s²+2ζωns+ωn²)","K/s²","K/(s³+s)"],
answer:1
},

{
question:"ζ represents",
options:["Natural frequency","Gain","Damping ratio","Time constant"],
answer:2
},

{
question:"ωn represents",
options:["Time constant","Natural frequency","Damping ratio","Gain"],
answer:1
},

{
question:"When ζ = 0, the system is",
options:["Overdamped","Underdamped","Undamped","Critically damped"],
answer:2
},

{
question:"When 0 < ζ < 1, the system is",
options:["Underdamped","Overdamped","Critically damped","Unstable"],
answer:0
},

{
question:"When ζ = 1, the system is",
options:["Undamped","Critically damped","Underdamped","Overdamped"],
answer:1
},

{
question:"When ζ > 1, the system is",
options:["Underdamped","Overdamped","Critically damped","Oscillatory"],
answer:1
},

{
question:"Rise time is defined as",
options:["Time to reach final value","Time to reach peak value","Time to rise from 10% to 90% of final value","Time to reach steady state"],
answer:2
},

{
question:"Peak time is defined as",
options:["Time taken to reach maximum value","Time taken to reach steady state","Time constant","Rise time"],
answer:0
},

{
question:"Maximum overshoot occurs in",
options:["Underdamped systems","Overdamped systems","Critically damped systems","First order systems"],
answer:0
},

{
question:"Settling time is defined as the time taken for response to reach",
options:["±2% of final value","±5% of final value","Final value exactly","Zero value"],
answer:0
},

{
question:"Steady state error is defined as",
options:["Initial error","Difference between input and output at steady state","Peak error","Maximum error"],
answer:1
},

{
question:"The steady state error depends on",
options:["System type","Input type","System parameters","All of the above"],
answer:3
},

{
question:"A step input represents",
options:["Constant input","Linearly increasing input","Sudden change input","Periodic input"],
answer:2
}

];

const quizArea = document.getElementById("quizArea");

if (quizArea) {

    questions.forEach((q, index) => {

        let html = `

        <div class="question-card">

            <h3>${index + 1}. ${q.question}</h3>

            ${q.options.map((opt, optIndex) =>

            `<label class="option">

                <input
                    type="radio"
                    name="q${index}"
                    value="${optIndex}">

                ${opt}

            </label>`

            ).join("")}

        </div>

        `;

        quizArea.innerHTML += html;

    });

}

function checkAnswers() {

    let score = 0;

    questions.forEach((q, index) => {

        const selected =
            document.querySelector(
                `input[name="q${index}"]:checked`
            );

        const optionLabels =
            document.querySelectorAll(
                `input[name="q${index}"]`
            );

        let selectedAnswer = -1;

        if (selected) {

            selectedAnswer =
                parseInt(selected.value);

            if (selectedAnswer === q.answer) {

                score++;

            }

        }

        optionLabels.forEach((radio, optIndex) => {

            const label =
                radio.parentElement;

            label.style.background = "";
            label.style.color = "";
            label.style.fontWeight = "";

            if (optIndex === q.answer) {

                label.style.background =
                    "#dcfce7";

                label.style.color =
                    "#166534";

                label.style.fontWeight =
                    "bold";

            }

            /* wrong selected answer */

            if (
                selectedAnswer !== q.answer &&
                optIndex === selectedAnswer
            ) {

                label.style.background =
                    "#fee2e2";

                label.style.color =
                    "#dc2626";

                label.style.fontWeight =
                    "bold";

            }

        });

    });

    const percentage =
        ((score / questions.length) * 100)
        .toFixed(2);

    let resultColor =
        percentage >= 50
            ? "#16a34a"
            : "#dc2626";

    let resultText =
        percentage >= 50
            ? "PASS ✅"
            : "FAIL ❌";

    document.getElementById("resultBox").innerHTML = `

    <div class="result-card">

        <h2>Your Score</h2>

        <h1>${score}/${questions.length}</h1>

        <h3>Percentage : ${percentage}%</h3>

        <h3 style="color:${resultColor}">
            ${resultText}
        </h3>

    </div>

    `;

    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    });

}
function resetQuiz() {

    document
        .querySelectorAll(
            'input[type="radio"]'
        )
        .forEach(radio => {

            radio.checked = false;

            radio.parentElement.style.background = "";
            radio.parentElement.style.color = "";
            radio.parentElement.style.fontWeight = "";

        });

    document.getElementById("resultBox").innerHTML = "";

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}