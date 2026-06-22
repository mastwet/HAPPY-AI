const fs = require('fs');
const path = process.argv[2];
const content = fs.readFileSync(path, 'utf-8');
const lines = content.split('\n');
const counts = {};
for (let i = 0; i < lines.length; i++) {
  const m = lines[i].match(/^```([a-zA-Z0-9_-]*)/);
  if (m) {
    const lang = m[1] || '(empty)';
    counts[lang] = (counts[lang] || 0) + 1;
  }
}
console.log(counts);
