const { log } = console;

export class User {
  constructor({ userName, ip, status }) {
    (this.userName = userName), (this.ip = ip ?? "localhost");
    this.status = status ?? true;
  }

  showdata() {
    log(`
    Soy ${this.userName}
    IP ADDRESS ${this.ip}
    Mi status es : ${this.status ? "🟢" : "❌"}
    `);
  }

  changeStatus = () => (this.status = !this.status);
}
