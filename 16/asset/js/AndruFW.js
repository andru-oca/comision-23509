export class AndruFW {
  constructor(containerID) {
    this.container = document.getElementById(containerID);
  }

  render(HTML) {
    this.container.innerHTML = HTML;
  }
}
