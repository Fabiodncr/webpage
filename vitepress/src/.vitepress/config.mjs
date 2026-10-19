import { defineConfig } from 'vitepress'

export default defineConfig(({ command }) => {
  // command sarà esattamente 'build' quando compili e 'dev' quando sviluppi
  const isBuild = command === 'build'
  


  return {
    // Se stiamo compilando usiamo il path di GitHub, altrimenti la radice
    base: isBuild ? '/webpage/' : '/', 
    
    title: "Fabio Di Nocera",
    description: "...writing about physics & maths",
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
            { text: 'Comunicazione', link: '/comunicazione' },
            { text: 'Didattica', link: '/didattica' }
          ],
          
          outline: {
            level: 2,
            label: 'In questa pagina' 
          },

          sidebar: [
            {
              text: 'Menu',
              items: [
                { text: 'Home', link: '/' },
                { text: 'Ricerca', link: '/ricerca' },
                { text: 'Comunicazione', link: '/comunicazione' },
                {
                  text: 'Didattica', 
                  link: '/didattica',
                  collapsed: true,
                  items: [
                    { text: 'Argomento 1', link: '/didattica/arg-1' },
                  ]
                }
              ]
            }
          ]
        }   
      },

      en: {
        label: 'English',
        lang: 'en',
        link: '/en/',
        
        outline: {
          level: 2,
          label: 'On this page' 
        },

        themeConfig: {
          nav: [
            { text: 'Home', link: '/en/index' },
            { text: 'Research', link: '/en/ricerca' },
            { text: 'Communication', link: '/en/comunicazione' },
            { text: 'Teaching', link: '/en/didattica' }
          ],

          sidebar: [
            {
              text: 'Menu',
              items: [
                { text: 'Home', link: '/en/index' },
                { text: 'Research', link: '/en/ricerca' },
                { text: 'Communication', link: '/en/comunicazione' },
                { 
                  text: 'Teaching', 
                  link: '/en/didattica',
                  collapsed: true,
                  items: [
                    { text: 'Topic 1', link: '/en/didattica/arg-1' },
                  ]
                }
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
        { icon: 'gmail', link: 'mailto:fabiodncr@gmail.com' },
        { icon: 'github', link: 'https://github.com/Fabiodncr' },
        { icon: 'linkedin', link: 'https://www.linkedin.com/in/fabio-di-nocera-647123180' },
        { icon: 'googlescholar', link: 'https://scholar.google.com/citations?user=f4tI0xcAAAAJ&hl=en' }
      ]
    },
    
  }

  head: [
    ['link', { rel: 'stylesheet', href: 'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css' }]
  ]

})