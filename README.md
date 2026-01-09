<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
</head>

<body>

<h1>💬 Chat-Based LLMs with LangChain & Google Gemini</h1>

<h2>📘 Learning & Exploration Repository</h2>

<p>
This repository is a <strong>professional, learner-friendly continuation</strong> of the
<strong>Regular LLMs with LangChain & Google Gemini</strong> project.
It focuses on <strong>chat-based Large Language Models (LLMs)</strong> using
<strong>ChatGoogleGenerativeAI</strong>, helping learners understand how conversational AI
systems work in practice.
</p>

<p>
The repository combines <strong>conceptual clarity</strong> with
<strong>hands-on implementation</strong>, making it ideal for students, beginners,
and aspiring GenAI engineers.
</p>

<hr>

<div class="section">
<h2>🧠 Foundations: What This Repository Is About</h2>

<h3>What Are Chat-Based LLMs?</h3>
<p>
Chat-based LLMs are designed for <strong>multi-turn conversations</strong>.
Unlike regular LLMs that process a single prompt at a time, chat models:
</p>

<ul>
    <li>Maintain conversational context</li>
    <li>Understand message roles (system, user, assistant)</li>
    <li>Enable natural, assistant-like interactions</li>
</ul>

<p>
This repository demonstrates how to build such systems using
<strong>Google Gemini</strong> through <strong>LangChain’s chat model interface</strong>.
</p>
</div>

<hr>

<div class="section">
<h3>Why Use LangChain for Chat LLMs?</h3>
<p>
LangChain simplifies chat-based LLM development by:
</p>

<ul>
    <li>Structuring conversations using messages</li>
    <li>Managing conversational context</li>
    <li>Providing clean abstractions over Gemini APIs</li>
    <li>Supporting scalable and production-ready workflows</li>
</ul>
</div>

<hr>

<div class="section">
<h2>📂 Project Structure</h2>

<pre>
project/
├── files/
│   ├── .env        # API key configuration
│   ├── main.py     # Streamlit chat interface
│   └── req.txt     # Required dependencies
├── Include/
├── Lib/
├── Scripts/
├── share/
├── langchain project.code-workspace
└── pyvenv.cfg
</pre>

<p>
The <strong>files/</strong> folder contains all application-specific files required
to run the project.
</p>
</div>

<hr>

<div class="section">
<h2>⚙️ Environment Setup (Step-by-Step)</h2>

<h3>1️⃣ Create a Virtual Environment</h3>
<pre><code>python -m venv project</code></pre>

<h3>2️⃣ Activate the Virtual Environment</h3>

<p><strong>Windows:</strong></p>
<pre><code>project\Scripts\activate</code></pre>

<p><strong>macOS / Linux:</strong></p>
<pre><code>source project/bin/activate</code></pre>

<h3>3️⃣ Install Required Dependencies</h3>
<pre><code>pip install -r req.txt</code></pre>

<p>
This installs LangChain, Google Generative AI integrations,
Streamlit, and python-dotenv.
</p>
</div>

<hr>

<div class="section">
<h2>🔐 API Key Management (dotenv)</h2>

<p>
To securely manage your API key:
</p>

<ol>
    <li>Create a <code>.env</code> file inside the <code>files/</code> folder</li>
    <li>Add your Google Gemini API key:</li>
</ol>

<pre><code>API_KEY="your_api_key_here"</code></pre>

<p>
The key is loaded at runtime using <strong>python-dotenv</strong>.
</p>
</div>

<hr>

<div class="section">
<h2>📘 File Explanation</h2>

>

<h3>1. Main.py (Streamlit Chat App)</h3>
<p>
This file provides a simple web-based chat interface using
<code>ChatGoogleGenerativeAI</code>.
</p>

<ul>
    <li>Streamlit-based UI</li>
    <li>Secure API loading via dotenv</li>
    <li>Real-time conversational interaction</li>
</ul>
</div>

<hr>

<div class="section">
<h2>▶️ Running the Application</h2>

<pre><code>streamlit run main.py</code></pre>

<p>
This launches a browser-based chat interface for interacting
with the Gemini chat model.
</p>
</div>

<hr>

<div class="section">
<h2>🎥 Video Demonstration</h2>

<p>
A video recording of the project execution is provided for reference.
</p>

<ul>
    <li>Virtual environment activation</li>
    <li>VS Code folder structure</li>
    <li>Live chat execution</li>
</ul>
















</div>




<div class="section">
<h2>🔗 Learning Path Recommendation</h2>

<p>
1️⃣ Regular LLMs with LangChain & Google Gemini<br>
2️⃣ Chat-Based LLMs with LangChain & Google Gemini
</p>

<p>
Both repositories are designed to work in sync for structured learning.
</p>
</div>

<section>
  <h3>🔹 OpenAI Chat Model (Reference Only)</h3>
  <p>
    An OpenAI chat model is included only to demonstrate workflow similarity
    with Google Gemini when used via LangChain.
  </p>
  <p>
    Execution requires a valid OpenAI API subscription and enabled chat models.
    Without API access, this code will not run and is provided strictly for
    reference and flow understanding purposes.
  </p>
</section>


<hr>

<p>
⭐ If this repository helped you understand chat-based LLMs,
consider starring it and sharing it with other learners.
</p>

<p>
<strong>Author:</strong> Shrutika Kapade<br>
Data Science | GenAI | LangChain Enthusiast
</p>

</body>
</html>
