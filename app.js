import React, { useState } from "react";
import { Container, Button, TextField, MenuItem } from "@mui/material";

function App() {
  const [selectedReport, setSelectedReport] = useState("");
  const [format, setFormat] = useState("csv");
  const [outputDir, setOutputDir] = useState("");

  const handleGenerateReport = () => {
    // Chamada à API para gerar o relatório
  };

  return (
    <Container>
      <h1>ODIN Report Generator</h1>
      <TextField
        label="Output Directory"
        fullWidth
        value={outputDir}
        onChange={(e) => setOutputDir(e.target.value)}
      />
      <TextField
        select
        label="Select Report Type"
        fullWidth
        value={selectedReport}
        onChange={(e) => setSelectedReport(e.target.value)}
      >
        <MenuItem value="performance">Performance Report</MenuItem>
        <MenuItem value="security">Security Report</MenuItem>
      </TextField>
      <TextField
        select
        label="Select Format"
        fullWidth
        value={format}
        onChange={(e) => setFormat(e.target.value)}
      >
        <MenuItem value="csv">CSV</MenuItem>
        <MenuItem value="powerbi">Power BI</MenuItem>
      </TextField>
      <Button onClick={handleGenerateReport}>Generate Report</Button>
    </Container>
  );
}

export default App;
