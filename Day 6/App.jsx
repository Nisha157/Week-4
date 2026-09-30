import { useEffect, useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/tasks/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch tasks");
        }
        return response.json();
      })
      .then((data) => {
        setTasks(data.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("API Error:", error);
        setError("Unable to connect to Django API.");
        setLoading(false);
      });
  }, []);

  return (
    <div
      style={{
        maxWidth: "800px",
        margin: "40px auto",
        padding: "20px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <h1>Task Management System</h1>

      {loading && <p>Loading tasks...</p>}

      {error && <p>{error}</p>}

      {!loading && !error && tasks.length === 0 && (
        <p>No tasks available.</p>
      )}

      {!loading && !error && tasks.length > 0 && (
        <div>
          {tasks.map((task) => (
            <div
              key={task.id}
              style={{
                border: "1px solid #ddd",
                borderRadius: "8px",
                padding: "16px",
                marginBottom: "12px",
              }}
            >
              <h2>{task.name}</h2>
              <p>{task.description}</p>
              <p>
                <strong>Status:</strong> {task.status}
              </p>
              <p>
                <strong>Created:</strong>{" "}
                {new Date(task.created_at).toLocaleDateString("en-IN", {
  day: "2-digit",
  month: "short",
  year: "numeric",
})}{" "}
{new Date(task.created_at).toLocaleTimeString("en-IN", {
  hour: "2-digit",
  minute: "2-digit",
})}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;