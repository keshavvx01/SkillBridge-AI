import { useState } from "react";

function App() {
  const [skills, setSkills] = useState("");
  const [role, setRole] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const handleAnalyze = async () => {
  setLoading(true);   // start loading

  try {
    const response = await fetch("http://127.0.0.1:8000/api/analyze/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        skills: skills.split(",").map(s => s.trim()),
        role: role,
      }),
    });

    const data = await response.json();
    setResult(data);

  } catch (err) {
    console.error(err);
  }

  setLoading(false);  // stop loading
};

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>SkillBridge AI</h1>

      <div>
        <input
          placeholder="Enter skills (e.g. Python,Docker)"
          value={skills}
          onChange={(e) => setSkills(e.target.value)}
          style={{ width: "300px", padding: "8px" }}
        />
      </div>

      <br />

      <div>
        <input
          placeholder="Enter role (e.g. DevOps Engineer)"
          value={role}
          onChange={(e) => setRole(e.target.value)}
          style={{ width: "300px", padding: "8px" }}
        />
      </div>

      <br />

      <button onClick={handleAnalyze} style={{ padding: "10px 20px" }}>
        Analyze
      </button>
       {loading && <p>⏳ Processing...</p>}
      <br /><br />

      {result && (
        <div>
          <h2>Score: {result.score}%</h2>
          <p><b>Matched:</b> {result.matched.join(", ")}</p>
          <p><b>Missing:</b> {result.missing.join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default App;
