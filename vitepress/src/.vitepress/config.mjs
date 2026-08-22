import { defineConfig } from 'vitepress'

export default defineConfig(({ command }) => {
  // command sarà esattamente 'build' quando compili e 'dev' quando sviluppi
  const isBuild = command === 'build'
  


  return {
    // Se stiamo compilando usiamo il path di GitHub, altrimenti la radice
    base: isBuild ? '/webpage/' : '/', 
    
    title: "Fabio Di Nocera",
    description: "Ricercatore in Fisica",
    srcDir: '.',
    markdown: {
      math: true,
      lineNumbers: true
    },

    locales: {
      root: {
        label: 'Italiano',
        lang: 'it',
        
        themeConfig: {
          nav: [
            { text: 'Home', link: '/' },
            { text: 'Ricerca', link: '/ricerca' },
            { text: 'Didattica', link: '/didattica' },
            { text: 'Comunicazione', link: '/comunicazione' },
          ],
          
          sidebar: [
            {
              text: 'Menu',
              items: [
                { text: 'Home', link: '/' },
                { text: 'Ricerca', link: '/ricerca' },
                {
                  text: 'Didattica', 
                  link: '/didattica',
                  collapsed: true,
                  items: [
                    { text: 'Lezione 1', link: '/didattica/lezione-1' },
                    { text: 'Lezione 2', link: '/didattica/lezione-2' },
                    { text: 'Lezione 3', link: '/didattica/lezione-3' }
                  ]
                },
                { text: 'Comunicazione', link: '/comunicazione' }
              ]
            }
          ]
        }   
      },

      en: {
        label: 'English',
        lang: 'en',
        link: '/en/',

        themeConfig: {
          nav: [
            { text: 'Home', link: '/en/index' },
            { text: 'Research', link: '/en/ricerca' },
            { text: 'Teaching', link: '/en/didattica' },
            { text: 'Communication', link: '/en/comunicazione' }
          ],

          sidebar: [
            {
              text: 'Menu',
              items: [
                { text: 'Home', link: '/en/index' },
                { text: 'Research', link: '/en/ricerca' },
                { 
                  text: 'Teaching', 
                  link: '/en/didattica',
                  collapsed: true,
                  items: [
                    { text: 'Lesson 1', link: '/en/didattica/lezione-1' },
                    { text: 'Lesson 2', link: '/en/didattica/lezione-2' },
                    { text: 'Lesson 3', link: '/en/didattica/lezione-3' }
                  ]
                },
                { text: 'Communication', link: '/en/comunicazione' },
              ]
            }
          ]
        }
      }
    },
  
    vue: {
      template: {
        compilerOptions: {
          isCustomElement: (tag) => tag.startsWith('annotation') || tag.startsWith('math') || tag.startsWith('mspace') || tag.startsWith('mrow') || tag.startsWith('mo') || tag.startsWith('mn') || tag.startsWith('mi') || tag.startsWith('msup')
        }
      }
    },
    
    themeConfig: {
      socialLinks: [
        { icon: 'github', link: 'https://github.com/Fabiodncr' },
        { icon: 'linkedin', link: 'https://linkedin.com' }
      ]
    } 
  }

  head: [
    ['link', { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css' }]
  ]

})