import { useState } from "react";

function App() {
  const [skills, setSkills] = useState("");
  const [role, setRole] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/analyze/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        skills: skills.split(","),
        role: role,
      }),
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>SkillBridge AI</h1>

      <input
        placeholder="Enter skills (comma separated)"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
      />

      <br /><br />

      <input
        placeholder="Enter role"
        value={role}
        onChange={(e) => setRole(e.target.value)}
      />

      <br /><br />

      <button onClick={handleSubmit}>Analyze</button>

      {result && (
        <div>
          <h2>Score: {result.score}%</h2>
          <p>Matched: {result.matched.join(", ")}</p>
          <p>Missing: {result.missing.join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default App;
