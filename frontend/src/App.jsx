

import { useState } from "react";
import axios from "axios";

function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeRepo = async () => {
    if (!repoUrl.trim()) {
      alert("Please enter a GitHub repository URL");
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/analyze",
        {
          repo_url: repoUrl,
        }
      );

      setResult(response.data.analysis);
    } catch (error) {
      console.error(error);

      setResult({
        purpose: "Error",
        tech_stack: "Error",
        architecture: "Error",
        summary: "Failed to analyze repository.",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="background-glow"></div>

      <div className="container">
        <header className="header">
          <h1>CodePilot AI</h1>
          <p>Multi-Agent GitHub Repository Analysis Platform</p>
        </header>

        <section className="hero-card">
          <h2>Analyze GitHub Repository</h2>

          <p className="subtitle">
            Understand architecture, dependencies, code quality and
            repository structure using AI-powered analysis.
          </p>

          <div className="input-row">
            <input
              type="text"
              placeholder="https://github.com/user/repository"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
            />

            <button
              onClick={analyzeRepo}
              disabled={loading}
            >
              {loading
                ? "Analyzing..."
                : "Analyze Repository"}
            </button>
          </div>
        </section>

        <section className="stats">
          <div className="stat-card">
            <h3>⚡ AI</h3>
            <span>Repository Analysis</span>
          </div>

          <div className="stat-card">
            <h3>📂 GitHub</h3>
            <span>Repository Scanner</span>
          </div>

          <div className="stat-card">
            <h3>🧠 DeepSeek</h3>
            <span>LLM Engine</span>
          </div>
        </section>

        <section className="results">
          <h2>Analysis Results</h2>

          {loading ? (
            <div className="result-card">
              <h3>⚡ AI Working...</h3>

              <p>
                Cloning Repository...
                <br />
                Reading Files...
                <br />
                Understanding Architecture...
                <br />
                Generating Insights...
              </p>
            </div>
          ) : result ? (
            <div className="analysis-grid">
              <div className="analysis-card">
                <h3>🎯 Purpose</h3>
                <p>{result.purpose}</p>
              </div>

              <div className="analysis-card">
                <h3>⚙️ Tech Stack</h3>
                <p>{result.tech_stack}</p>
              </div>

              <div className="analysis-card full-width">
                <h3>🏗 Architecture</h3>
                <p>{result.architecture}</p>
              </div>

              <div className="analysis-card full-width">
                <h3>📝 Summary</h3>
                <p>{result.summary}</p>
              </div>
            </div>
          ) : (
            <div className="result-card">
              <h3>Ready To Analyze</h3>

              <p>
                Paste a GitHub repository URL and click Analyze Repository.
              </p>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

export default App;