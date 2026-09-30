import { useEffect, useState } from "react";
import "./App.css";

const API = "http://127.0.0.1:8000/api/tasks/";

function App() {
  const [tasks, setTasks] = useState([]);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const loadTasks = () => {
    fetch(API)
      .then((res) => res.json())
      .then((data) => setTasks(data.data));
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const addTask = (e) => {
    e.preventDefault();

    fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name,
        description,
        status: "Pending",
      }),
    }).then(() => {
      setName("");
      setDescription("");
      loadTasks();
    });
  };

  return (
    <div className="app">
      <h1>Task Tracker</h1>
      <p>Task Tracker Backend API</p>

      <form onSubmit={addTask}>
        <input
          placeholder="Task name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <button>Add Task</button>
      </form>

      <h2>All Tasks</h2>

      {tasks.map((task) => (
        <div className="task" key={task.id}>
          <h3>{task.name}</h3>
          <p>{task.description}</p>
          <span>{task.status}</span>
          <small>
            Created: {new Date(task.created_at).toLocaleString()}
          </small>
        </div>
      ))}
    </div>
  );
}

export default App;