let header = getHeader();
export const base = `${header}/api`;

function getHeader() {
  var head = "";
  switch (process.env.NODE_ENV) {
    case "development":
      head = ""; //开发环境url
      break;
    case "production":
      //http://localhost:8082
      head = location.protocol + "//" + location.host; //生产环境url
      break;
  }
  return head;
}
