import { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";

function App() {
  const [status, setStatus] = useState("...");
  useEffect(() => {
    fetch("/api/health")
      .then((r) => r.json())
      .then((d) => setStatus(d.status))
      .catch(() => setStatus("нет связи с сервером"));
  }, []);
  return (
    <div>
      <h1>АС «Зачетка»</h1>
      <p>Статус сервера: {status}</p>
    </div>
  );
}

createRoot(document.getElementById("root")!).render(<App />);
