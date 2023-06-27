class BookCard extends HTMLElement {
  //observer attributes goes first babe
  static get observedAttributes() {
    return ['thename', 'caption', 'img', 'bgimg', 'leadto', 'estado'];
  }
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  attributeChangedCallback(attr, oldVal, newVal) {
    if (attr === 'thename') {
      this.thename = newVal;
    }
    if (attr === 'caption') {
      this.caption = newVal;
    }
    if (attr === 'img') {
      this.img = newVal;
    }
    if (attr === 'bgimg') {
      this.bgimg = newVal;
    }
    if (attr === 'leadto') {
      this.leadto = newVal;
    }
    if (attr === 'estado') {
      this.estado = newVal;
    }
  }
  makeTemplate() {
    const template = document.createElement('template');
    template.innerHTML = `
    <style>${this.getStyles()}</style>
    <section class="custom_element">
      <div class="card_inner">
        <!--Card's Front-face-->
        <div class="card_face card_face-front">
          <div class="estado"></div>
          <div class="img_container">
            <img
              class="card_face-image"
              src="${this.img}"
              alt="picture project"
            />
          </div>
          <div class="card_description">
            <p class="project_name">${this.thename}</p>
            <div class="flip_container">
              <p class="watch_project">${this.caption}</p>
              <p class="arrow">Más info</p>
            </div>
          </div>
        </div>
        <!--Card's Back-face-->
        <div class="card_face card_face-back">
          <ul class="card_caption">
            <li><strong>Título:</strong><slot name="titulo"></slot></li> 
            <li><strong>Editorial:</strong><slot name="editorial"></slot></li> 
            <li><strong>Autores:</strong><slot name="autores"></slot></li> 
            <li><strong>Año de Publicación:</strong><slot name="año"></slot></li> 
            <li><strong>Idioma:</strong><slot name="idioma"></slot></li> 
            <li><strong>ISBN:</strong><slot name="isbn"></slot></li> 
            <li><strong>Categoría:</strong><slot name="categoria"></slot></li> 
          </ul>
        </div>
      </div>
    </section>
    `;
    return template;
  }
  getStyles() {
    return `

      * {
        padding: 0;
        margin: 0;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
      }
      .custom_element {
        font-size: 16px;
        font-weight: 500;
        display: block;
        width: 19.125em;
        height: 21.875em;
        border-radius: 1em;
        -webkit-perspective: 1000px;
                perspective: 1000px;
      }
      @media (max-width: 480px) {
        .custom_element {
          font-size: 13px;
          width: 300px;
        }
      }

      .custom_element .flipped {
        -webkit-transform: rotateY(180deg);
                transform: rotateY(180deg);
      }

      .custom_element .card_inner {
        width: 100%;
        height: 100%;
        position: relative;
        border-radius: 1em;
        -webkit-transform-style: preserve-3d;
                transform-style: preserve-3d;
        -webkit-transition: transform 1.5s ease;
        transition: transform 1.5s ease;
      }

      .custom_element .card_inner .card_face {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        -webkit-backface-visibility: hidden;
                backface-visibility: hidden;
        overflow: hidden;
        border-radius: 1em;
        -webkit-box-shadow: 0em 0.3125em 0.625em rgba(0, 0, 0, 0.25);
                box-shadow: 0em 0.3125em 0.625em rgba(0, 0, 0, 0.25);
      }

      .custom_element .card_inner .card_face-front {
        background-color: #f4f4f4;
        position: relative;
      }

      .custom_element .card_inner .estado{
        position: absolute;
        top: 10px;
        right: 10px;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: ${this.estado};
      }

      .custom_element .card_inner .card_face-front .img_container {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -ms-flex-wrap: wrap;
            flex-wrap: wrap;
        -webkit-box-orient: vertical;
        -webkit-box-direction: normal;
            -ms-flex-direction: column;
                flex-direction: column;
        -webkit-box-pack: center;
            -ms-flex-pack: center;
                justify-content: center;
        -webkit-box-align: center;
            -ms-flex-align: center;
                align-items: center;
        height: 80%;
        background-color: #212121;
        overflow: hidden;
      }

      .custom_element .card_inner .card_face-front .img_container .card_face-image {
        width: 100%;
        height: auto;
        margin: auto;
      }

      .custom_element .card_inner .card_face-front .card_description {
        margin: 0 auto;
        width: 100%;
        height: 20%;
        padding-left: 0.6em;
        padding-right: 0.6em;
        border-radius: 0 0 1.25em 1.25em;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -ms-flex-wrap: wrap;
            flex-wrap: wrap;
        -webkit-box-orient: vertical;
        -webkit-box-direction: normal;
            -ms-flex-direction: column;
                flex-direction: column;
        -webkit-box-pack: space-evenly;
            -ms-flex-pack: space-evenly;
                justify-content: space-evenly;
        -webkit-box-align: space-evenly;
            -ms-flex-align: space-evenly;
                align-items: space-evenly;
      }

      .custom_element .card_inner .card_face-front .card_description .project_name {
        padding-top: 6px;
        font-size: 0.9em;
        font-weight: 500;
        color: #000;
        -webkit-transition: 0.2s all ease-in-out;
        transition: 0.2s all ease-in-out;
        text-decoration: none;
      }

      .custom_element .card_inner .card_face-front .card_description .flip_container {
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -ms-flex-wrap: wrap;
            flex-wrap: wrap;
        -webkit-box-orient: horizontal;
        -webkit-box-direction: normal;
            -ms-flex-direction: row;
                flex-direction: row;
        -webkit-box-pack: justify;
            -ms-flex-pack: justify;
                justify-content: space-between;
        -webkit-box-align: center;
            -ms-flex-align: center;
                align-items: center;
      }

      .custom_element .card_inner .card_face-front .card_description .flip_container .watch_project {
        font-size: 0.8em;
      }

      .custom_element .card_inner .card_face-front .card_description .flip_container .arrow {
        // width: 2.5em;
        // height: 2.5em;
        font-size: 0.8em;
        cursor: pointer;
        text-decoration: underline;
        -webkit-transition: 0.2s all ease-in-out;
        transition: 0.2s all ease-in-out;
      }

      .custom_element .card_inner .card_face-front .card_description .flip_container img:active {
        -webkit-transform: scale(0.9);
                transform: scale(0.9);
      }

      .custom_element .card_inner .card_face-back {
        -webkit-transform: rotateY(180deg);
                transform: rotateY(180deg);
        background-color: #fff;
        cursor: pointer;
      }

      .custom_element .card_inner .card_face-back .card_caption {
        width: 100%;
        height: 100%;
        line-height: 1.6em;
        padding: 0.5em 0.5em 0 0.5em;
        font-size: 0.8em;
        font-weight: 400;
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
      }
       .custom_element .card_inner .card_face-back .card_caption li {
        padding: 0.5em 1.7em 0 1.7em;
      }
      .custom_element .card_inner .card_face-back .card_caption li strong {
        margin-right: 5px;
      }
    `;
  }
  render() {
    this.shadowRoot.appendChild(this.makeTemplate().content.cloneNode(true));
  }
  getCard() {
    let projectCard = this.shadowRoot.querySelector('.card_inner');
    return projectCard;
  }
  flipCard() {
    setTimeout(() => this.getCard().classList.add('flipped'), 100);
  }
  removeFlipCard() {
    this.getCard().classList.remove('flipped');
  }
  /*************Connected Callback is requered!!************/
  connectedCallback() {
    //render template
    this.render();
    //use here addEventListeners
    let arrowBtn = this.shadowRoot.querySelector('.arrow');
    arrowBtn.addEventListener('click', () => {
      this.flipCard();
    });

    let backCard = this.shadowRoot.querySelector('.card_face-back');
    backCard.addEventListener('click', () => {
      this.removeFlipCard();
    });
  }
  disconectedCallback() {
    //use here removeEventListeners
  }
}

customElements.define('book-card', BookCard);
