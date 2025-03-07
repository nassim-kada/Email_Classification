document.getElementById("classify-btn").addEventListener("click", async function () {
    const emailContent = document.getElementById("email-content").value;

    if (!emailContent.trim()) {
        alert("Please enter email content.");
        return;
    }

    document.getElementById("loading").style.display = "block";
    document.getElementById("result-section").style.display = "none";

    try {
        const response = await fetch("https://email-classification-7m9y.onrender.com/classify", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email_content: emailContent })
        });

        const data = await response.json();
        document.getElementById("loading").style.display = "none";

        if (data.error) {
            alert("Error: " + data.error);
            return;
        }

        document.getElementById("result-box").textContent = `Prediction: ${data.prediction.toUpperCase()}`;
        document.getElementById("spam-percent").textContent = data.spam_probability;
        document.getElementById("ham-percent").textContent = data.ham_probability;
        document.getElementById("result-section").style.display = "block";
    } catch (error) {
        document.getElementById("loading").style.display = "none";
        alert("Failed to connect to the server. Make sure Flask is running.");
    }
});

document.getElementById("clear-btn").addEventListener("click", function () {
    document.getElementById("email-content").value = "";
    document.getElementById("result-section").style.display = "none";
});