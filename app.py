from flask import Flask, render_template_string, request, session
import json
import sys

app = Flask(__name__)
app.secret_key = 'anshika_8795109203'  # Change this to a secure key
PASSWORD = '@Kernelintiate/directivesqlinjectF8795109203/exploitallFALSEport500.overrequest'  # Set your password here

assembly_code_line = '''
section .data
    msg db 'Authentication successful', 0
    len equ $ - msg

section .bss
    res resb 1

section .text
    global _start

_start:
    ; Write message to stdout
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, len
    int 0x80

    ; Exit
    mov eax, 1
    xor ebx, ebx
    int 0x80
'''
assembly_code = assembly_code_line * 50

password_form = f'''
<!doctype html>
<html>
<head>
    <style>
        body {{
            background-color: black;
            color: green;
            font-family: monospace;
            font-size: 16px;
            overflow: hidden;
        }}
        h2 {{
            color: green;
        }}
        .scroll {{
            position: relative;
            height: 200px;
            overflow: hidden;
        }}
        .scroll pre {{
            color: lightgreen;
            font-size: 10px;
            animation: blink 0.05s step-end infinite, scroll 20s linear infinite;
        }}
        input[type=password] {{
            background-color: black;
            color: green;
            border: 1px solid green;
            font-family: monospace;
            font-size: 16px;
        }}
        input[type=submit] {{
            background-color: black;
            color: green;
            border: 1px solid green;
            font-family: monospace;
            font-size: 16px;
        }}
        @keyframes blink {{
            from, to {{
                visibility: hidden;
            }}
            50% {{
                visibility: visible;
            }}
        }}
        @keyframes scroll {{
            from {{
                transform: translateY(100%);
            }}
            to {{
                transform: translateY(-100%);
            }}
        }}
    </style>
    <title>Password Verification</title>
</head>
<body>
    <h2>Enter password:</h2>
    <form method="post" action="/verify">
      <input type="password" name="password">
      <input type="submit" value="Submit">
    </form>
    <div class="scroll">
        <pre>{assembly_code}</pre>
    </div>
</body>
</html>
'''

success_page = '''
<!doctype html>
<html>
<head>
    <style>
        body {
            background-color: black;
            color: green;
            font-family: monospace;
            font-size: 10px;
            margin: 0;
            overflow: hidden;
            height: 100vh;
        }
        #loader {
            position: absolute;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: black;
            color: green;
        }
        #progress-bar {
            width: 0;
            height: 30px;
            background-color: green;
            transition: width 0.1s linear;
        }
        #json-container {
            display: none;
            white-space: pre-wrap;
            color: lightgreen;
            padding: 20px;
            height: calc(100vh - 40px);
            overflow: auto;
        }
    </style>
</head>
<body>
    <div id="loader">
        <div>
            <div id="progress-bar"></div>
            <p>Loading...ACCESSING TO ANSHIKA : IN : +918795109203 / REMOVING LEAKS /exploitallFALSEport500.overrequest
            const express = require('express');
const axios = require('axios');
const app = express();
const port = 8080;

app.use(express.static('public'));

app.get('/quote', async (req, res) => {
  try {
    const response = await axios.get('https://api.quotable.io/random');
    res.send(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching quote');
  }
});

app.listen(port, () => {
  console.log(`Pomodoro app listening at http://localhost:${port}`);
});</p>
        </div>
    </div>
    <div id="json-container">
        <h2>
        Loading...ACCESSING TO ANSHIKA : IN : +918795109203 / REMOVING LEAKS /exploitallFALSEport500.overrequest {founded 3+ ongoing leaks on pornhub,onlyfans and darkweb}:</h2>
        <pre>{    },
    "node_modules/supports-preserve-symlinks-flag": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
      "integrity": "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==",
      "engines": {
        "node": ">= 0.4"
      },
      "funding": {
        "url": "https://github.com/sponsors/ljharb"
      }
    },
    "node_modules/tapable": {
      "version": "2.2.1",
      "resolved": "https://registry.npmjs.org/tapable/-/tapable-2.2.1.tgz",
      "integrity": "sha512-GNzQvQTOIP6RyTfE2Qxb8ZVlNmw0n88vp1szwWRimP02mnTsx3Wtn5qRdqY9w2XduFNUgvOwhNnQsjwCp+kqaQ==",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/terser": {
      "version": "5.19.2",
      "resolved": "https://registry.npmjs.org/terser/-/terser-5.19.2.tgz",
      "integrity": "sha512-qC5+dmecKJA4cpYxRa5aVkKehYsQKc+AHeKl0Oe62aYjBL8ZA33tTljktDHJSaxxMnbI5ZYw+o/S2DxxLu8OfA==",
      "dependencies": {
        "@jridgewell/source-map": "^0.3.3",
        "acorn": "^8.8.2",
        "commander": "^2.20.0",
        "source-map-support": "~0.5.20"
      },
      "bin": {
        "terser": "bin/terser"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/terser-webpack-plugin": {
      "version": "5.3.9",
      "resolved": "https://registry.npmjs.org/terser-webpack-plugin/-/terser-webpack-plugin-5.3.9.tgz",
      "integrity": "sha512-ZuXsqE07EcggTWQjXUj+Aot/OMcD0bMKGgF63f7UxYcu5/AJF53aIpK1YoP5xR9l6s/Hy2b+t1AM0bLNPRuhwA==",
      "dependencies": {
        "@jridgewell/trace-mapping": "^0.3.17",
        "jest-worker": "^27.4.5",
        "schema-utils": "^3.1.1",
        "serialize-javascript": "^6.0.1",
        "terser": "^5.16.8"
      },
      "engines": {
        "node": ">= 10.13.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/webpack"
      },
      "peerDependencies": {
        "webpack": "^5.1.0"
      },
      "peerDependenciesMeta": {
        "@swc/core": {
          "optional": true
        },
        "esbuild": {
          "optional": true
        },
        "uglify-js": {
          "optional": true
        }
      }
    },
    "node_modules/terser-webpack-plugin/node_modules/schema-utils": {
      "version": "3.3.0",
      "resolved": "https://registry.npmjs.org/schema-utils/-/schema-utils-3.3.0.tgz",
      "integrity": "sha512-pN/yOAvcC+5rQ5nERGuwrjLlYvLTbCibnZ1I7B1LaiAz9BRBlE9GMgE/eqV30P7aJQUf7Ddimy/RsbYO/GrVGg==",
      "dependencies": {
        "@types/json-schema": "^7.0.8",
        "ajv": "^6.12.5",
        "ajv-keywords": "^3.5.2"
      },
      "engines": {
        "node": ">= 10.13.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/webpack"
      }
    },
    "node_modules/terser/node_modules/commander": {
      "version": "2.20.3",
      "resolved": "https://registry.npmjs.org/commander/-/commander-2.20.3.tgz",
      "integrity": "sha512-GpVkmM8vF2vQUkj2LvZmD35JxeJOLCwJ9cUkugyk2nuhbv3+mJvpLYYt+0+USMxE+oj+ey/lJEnhZw75x/OMcQ=="
    },
    "node_modules/three": {
      "version": "0.134.0",
      "resolved": "https://registry.npmjs.org/three/-/three-0.134.0.tgz",
      "integrity": "sha512-LbBerg7GaSPjYtTOnu41AMp7tV6efUNR3p4Wk5NzkSsNTBuA5mDGOfwwZL1jhhVMLx9V20HolIUo0+U3AXehbg=="
    },
    "node_modules/thunky": {
      "version": "1.1.0",
      "resolved": "https://registry.npmjs.org/thunky/-/thunky-1.1.0.tgz",
      "integrity": "sha512-eHY7nBftgThBqOyHGVN+l8gF0BucP09fMo0oO/Lb0w1OF80dJv+lDVpXG60WMQvkcxAkNybKsrEIE3ZtKGmPrA=="
    },
    "node_modules/to-fast-properties": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz",
      "integrity": "sha512-/OaKK0xYrs3DmxRYqL/yDc+FxFUVYhDlXMhRmv3z915w2HF1tnN1omB354j8VUGO/hbRzyD6Y3sA7v7GS/ceog==",
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/to-regex-range": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
      "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
      "dependencies": {
        "is-number": "^7.0.0"
      },
      "engines": {
        "node": ">=8.0"
      }
    },
    "node_modules/toidentifier": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.1.tgz",
      "integrity": "sha512-o5sSPKEkg/DIQNmH43V0/uerLrpzVedkUh8tGNvaeXpfpuwjKenlSox/2O/BTlZUtEe+JG7s5YhEz608PlAHRA==",
      "engines": {
        "node": ">=0.6"
      }
    },
    "node_modules/tslib": {
      "version": "2.6.2",
      "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.6.2.tgz",
      "integrity": "sha512-AEYxH93jGFPn/a2iVAwW87VuUIkR1FVUKB77NwMF7nBTDkDrrT/Hpt/IrCJ0QXhW27jTBDcf5ZY7w6RiqTMw2Q=="
    },
    "node_modules/type-is": {
      "version": "1.6.18",
      "resolved": "https://registry.npmjs.org/type-is/-/type-is-1.6.18.tgz",
      "integrity": "sha512-TkRKr9sUTxEH8MdfuCSP7VizJyzRNMjj2J2do2Jr3Kym598JVdEksuzPQCnlFPW4ky9Q+iA+ma9BGm06XQBy8g==",
      "dependencies": {
        "media-typer": "0.3.0",
        "mime-types": "~2.1.24"
      },
      "engines": {
        "node": ">= 0.6"
      }
    },
    "node_modules/unicode-canonical-property-names-ecmascript": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/unicode-canonical-property-names-ecmascript/-/unicode-canonical-property-names-ecmascript-2.0.0.tgz",
      "integrity": "sha512-yY5PpDlfVIU5+y/BSCxAJRBIS1Zc2dDG3Ujq+sR0U+JjUevW2JhocOF+soROYDSaAezOzOKuyyixhD6mBknSmQ==",
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/unicode-match-property-ecmascript": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/unicode-match-property-ecmascript/-/unicode-match-property-ecmascript-2.0.0.tgz",
      "integrity": "sha512-5kaZCrbp5mmbz5ulBkDkbY0SsPOjKqVS35VpL9ulMPfSl0J0Xsm+9Evphv9CoIZFwre7aJoa94AY6seMKGVN5Q==",
      "dependencies": {
        "unicode-canonical-property-names-ecmascript": "^2.0.0",
        "unicode-property-aliases-ecmascript": "^2.0.0"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/unicode-match-property-value-ecmascript": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/unicode-match-property-value-ecmascript/-/unicode-match-property-value-ecmascript-2.1.0.tgz",
      "integrity": "sha512-qxkjQt6qjg/mYscYMC0XKRn3Rh0wFPlfxB0xkt9CfyTvpX1Ra0+rAmdX2QyAobptSEvuy4RtpPRui6XkV+8wjA==",
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/unicode-property-aliases-ecmascript": {
      "version": "2.1.0",
      "resolved": "https://registry.npmjs.org/unicode-property-aliases-ecmascript/-/unicode-property-aliases-ecmascript-2.1.0.tgz",
      "integrity": "sha512-6t3foTQI9qne+OZoVQB/8x8rk2k1eVy1gRXhV3oFQ5T6R1dqQ1xtin3XqSlx3+ATBkliTaR/hHyJBm+LVPNM8w==",
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/unpipe": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz",
      "integrity": "sha512-pjy2bYhSsufwWlKwPc+l3cN7+wuJlK6uz0YdJEOlQDbl6jo/YlPi4mb8agUkVC8BF7V8NuzeyPNqRksA3hztKQ==",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/update-browserslist-db": {
      "version": "1.0.11",
      "resolved": "https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.0.11.tgz",
      "integrity": "sha512-dCwEFf0/oT85M1fHBg4F0jtLwJrutGoHSQXCh7u4o2t1drG+c0a9Flnqww6XUKSfQMPpJBRjU8d4RXB09qtvaA==",
      "funding": [
        {
          "type": "opencollective",
          "url": "https://opencollective.com/browserslist"
        },
        {
          "type": "tidelift",
          "url": "https://tidelift.com/funding/github/npm/browserslist"
        },
        {
          "type": "github",
          "url": "https://github.com/sponsors/ai"
        }
      ],
      "dependencies": {
        "escalade": "^3.1.1",
        "picocolors": "^1.0.0"
      },
      "bin": {
        "update-browserslist-db": "cli.js"
      },
      "peerDependencies": {
        "browserslist": ">= 4.21.0"
      }
    },
    "node_modules/uri-js": {
      "version": "4.4.1",
      "resolved": "https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz",
      "integrity": "sha512-7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==",
      "dependencies": {
        "punycode": "^2.1.0"
      }
    },
    "node_modules/util-deprecate": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
      "integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw=="
    },
    "node_modules/utila": {
      "version": "0.4.0",
      "resolved": "https://registry.npmjs.org/utila/-/utila-0.4.0.tgz",
      "integrity": "sha512-Z0DbgELS9/L/75wZbro8xAnT50pBVFQZ+hUEueGDU5FN51YSCYM+jdxsfCiHjwNP/4LCDD0i/graKpeBnOXKRA=="
    },
    "node_modules/utils-merge": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/utils-merge/-/utils-merge-1.0.1.tgz",
      "integrity": "sha512-pMZTvIkT1d+TFGvDOqodOclx0QWkkgi6Tdoa8gC8ffGAAqz9pzPTZWAybbsHHoED/ztMtkv/VoYTYyShUn81hA==",
      "engines": {
        "node": ">= 0.4.0"
      }
    },
    "node_modules/uuid": {
      "version": "8.3.2",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-8.3.2.tgz",
      "integrity": "sha512-+NYs2QeMWy+GWFOEm9xnn6HCDp0l7QBD7ml8zLUmJ+93Q5NF0NocErnwkTkXVFNiX3/fpC6afS8Dhb/gz7R7eg==",
      "bin": {
        "uuid": "dist/bin/uuid"
      }
    },
    "node_modules/vary": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/vary/-/vary-1.1.2.tgz",
      "integrity": "sha512-BNGbWLfd0eUPabhkXUVm0j8uuvREyTh5ovRa/dyow/BqAbZJyC+5fU+IzQOzmAKzYqYRAISoRhdQr3eIZ/PXqg==",
      "engines": {
        "node": ">= 0.8"
      }
    },
    "node_modules/watchpack": {
      "version": "2.4.0",
      "resolved": "https://registry.npmjs.org/watchpack/-/watchpack-2.4.0.tgz",
      "integrity": "sha512-Lcvm7MGST/4fup+ifyKi2hjyIAwcdI4HRgtvTpIUxBRhB+RFtUh8XtDOxUfctVCnhVi+QQj49i91OyvzkJl6cg==",
      "dependencies": {
        "glob-to-regexp": "^0.4.1",
        "graceful-fs": "^4.1.2"
      },
      "engines": {
        "node": ">=10.13.0"
      }
    },
    "node_modules/wbuf": {
      "version": "1.7.3",
      "resolved": "https://registry.npmjs.org/wbuf/-/wbuf-1.7.3.tgz",
      "integrity": "sha512-O84QOnr0icsbFGLS0O3bI5FswxzRr8/gHwWkDlQFskhSPryQXvrTMxjxGP4+iWYoauLoBvfDpkrOauZ+0iZpDA==",
      "dependencies": {
        "minimalistic-assert": "^1.0.0"
      }
    },
    "node_modules/webpack": {
      "version": "5.88.2",
      "resolved": "https://registry.npmjs.org/webpack/-/webpack-5.88.2.tgz",
      "integrity": "sha512-JmcgNZ1iKj+aiR0OvTYtWQqJwq37Pf683dY9bVORwVbUrDhLhdn/PlO2sHsFHPkj7sHNQF3JwaAkp49V+Sq1tQ==",
      "dependencies": {
        "@types/eslint-scope": "^3.7.3",
        "@types/estree": "^1.0.0",
        "@webassemblyjs/ast": "^1.11.5",
        "@webassemblyjs/wasm-edit": "^1.11.5",
        "@webassemblyjs/wasm-parser": "^1.11.5",
        "acorn": "^8.7.1",
        "acorn-import-assertions": "^1.9.0",
        "browserslist": "^4.14.5",
        "chrome-trace-event": "^1.0.2",
        "enhanced-resolve": "^5.15.0",
        "es-module-lexer": "^1.2.1",
        "eslint-scope": "5.1.1",
        "events": "^3.2.0",
        "glob-to-regexp": "^0.4.1",
        "graceful-fs": "^4.2.9",
        "json-parse-even-better-errors": "^2.3.1",
        "loader-runner": "^4.2.0",
        "mime-types": "^2.1.27",
        "neo-async": "^2.6.2",
        "schema-utils": "^3.2.0",
        "tapable": "^2.1.1",
        "terser-webpack-plugin": "^5.3.7",
        "watchpack": "^2.4.0",
        "webpack-sources": "^3.2.3"
      },
      "bin": {
        "webpack": "bin/webpack.js"
      },
      "engines": {
        "node": ">=10.13.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/webpack"
      },
      "peerDependenciesMeta": {
        "webpack-cli": {
          "optional": true
        }
      }
    },
    "node_modules/webpack-cli": {
      "version": "4.10.0",
      "resolved": "https://registry.npmjs.org/webpack-cli/-/webpack-cli-4.10.0.tgz",
      "integrity": "sha512-NLhDfH/h4O6UOy+0LSso42xvYypClINuMNBVVzX4vX98TmTaTUxwRbXdhucbFMd2qLaCTcLq/PdYrvi8onw90w==",
      "dependencies": {
        "@discoveryjs/json-ext": "^0.5.0",
        "@webpack-cli/configtest": "^1.2.0",
        "@webpack-cli/info": "^1.5.0",
        "@webpack-cli/serve": "^1.7.0",
        "colorette": "^2.0.14",
        "commander": "^7.0.0",
        "cross-spawn": "^7.0.3",
        "fastest-levenshtein": "^1.0.12",
        "import-local": "^3.0.2",
        "interpret": "^2.2.0",
        "rechoir": "^0.7.0",
        "webpack-merge": "^5.7.3"
      },
      "bin": {
        "webpack-cli": "bin/cli.js"
      },
      "engines": {
        "node": ">=10.13.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/webpack"
      },
      "peerDependencies": {
        "webpack": "4.x.x || 5.x.x"
      },
      "peerDependenciesMeta": {
        "@webpack-cli/generators": {
          "optional": true
        },
        "@webpack-cli/migrate": {
          "optional": true
        },
        "webpack-bundle-analyzer": {
          "optional": true
        },
        "webpack-dev-server": {
          "optional": true
        }
      }
    },
    "node_modules/webpack-cli/node_modules/commander": {
      "version": "7.2.0",
      "resolved": "https://registry.npmjs.org/commander/-/commander-7.2.0.tgz",
      "integrity": "sha512-QrWXB+ZQSVPmIWIhtEO9H+gwHaMGYiF5ChvoJ+K9ZGHG/sVsa6yiesAD1GC/x46sET00Xlwo1u49RVVVzvcSkw==",
      "engines": {
        "node": ">= 10"
      }
    },
    "node_modules/webpack-dev-middleware": {
      "version": "5.3.3",
      "resolved": "https://registry.npmjs.org/webpack-dev-middleware/-/webpack-dev-middleware-5.3.3.tgz",
      "integrity": "sha512-hj5CYrY0bZLB+eTO+x/j67Pkrquiy7kWepMHmUMoPsmcUaeEnQJqFzHJOyxgWlq746/wUuA64p9ta34Kyb01pA==",
      "dependencies": {
        "colorette": "^2.0.10",
        "memfs": "^3.4.3",
        "mime-types": "^2.1.31",
        "range-parser": "^1.2.1",
        "schema-utils": "^4.0.0"
      },
      "engines": {
        "node": ">= 12.13.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/webpack"
      },
      "peerDependencies": {
        "webpack": "^4.0.0 || ^5.0.0"
      }
    },
    "node_modules/webpack-dev-middleware/node_modules/ajv": {
      "version": "8.12.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-8.12.0.tgz",
      "integrity": "sha512-sRu1kpcO9yLtYxBKvqfTeh9KzZEwO3STyX1HT+4CaDzC6HpTGYhIhPIzj9XuKU7KYDwnaeh5hcOwjy1QuJzBPA==",
      "dependencies": {
        "fast-deep-equal": "^3.1.1",
        "json-schema-traverse": "^1.0.0",
        "require-from-string": "^2.0.2",
        "uri-js": "^4.2.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/webpack-dev-middleware/node_modules/ajv-keywords": {
      "version": "5.1.0",
      "resolved": "https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-5.1.0.tgz",
      "integrity": "sha512-YCS/JNFAUyr5vAuhk1DWm1CBxRHW9LbJ2ozWeemrIqpbsqKjHVxYPyi5GC0rjZIT5JxJ3virVTS8wk4i/Z+krw==",
      "dependencies": {
        "fast-deep-equal": "^3.1.3"
      },
      "peerDependencies": {
        "ajv": "^8.8.2"
      }
    },
    "node_modules/webpack-dev-middleware/node_modules/json-schema-traverse": {
      "version": "1.0.0",
      "resolved": "https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-1.0.0.tgz",
      "integrity": "sha512-NM8/P9n3XjXhIZn1lLhkFaACTOURQXjWhV4BA/RnOv8xvgqtqpAX9IO4mRQxSx1Rlo4tqzeqb0sOlruaOy3dug=="
    },
    "node_modules/webpack-dev-middleware/node_modules/schema-utils": {
      "version": "4.2.0",
      "resolved": "https://registry.npmjs.org/schema-utils/-/schema-utils-4.2.0.tgz",
      "integrity": "sha512-L0jRsrPpjdckP3oPug3/VxNKt2trR8TcabrM6FOAAlvC/9Phcmm+cuAgTlxBqdBR1WJx7Naj9WHw+aOmheSVbw==",
      "dependencies": {
        "@types/json-schema": "^7.0.9",
        "ajv": "^8.9.0",
        "ajv-formats": "^2.1.1",
        "ajv-keywords": "^5.1.0"
      },
      "engines": {
        "node": ">= 12.13.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/webpack"
      }
    },
    "node_modules/webpack-dev-server": {
      "version": "4.15.1",
      "resolved": "https://registry.npmjs.org/webpack-dev-server/-/webpack-dev-server-4.15.1.tgz",
      "integrity": "sha512-5hbAst3h3C3L8w6W4P96L5vaV0PxSmJhxZvWKYIdgxOQm8pNZ5dEOmmSLBVpP85ReeyRt6AS1QJNyo/oFFPeVA==",
      "dependencies": {
        "@types/bonjour": "^3.5.9",
        "@types/connect-history-api-fallback": "^1.3.5",
        "@types/express": "^4.17.13",
        "@types/serve-index": "^1.9.1",
        "@types/serve-static": "^1.13.10",
        "@types/sockjs": "^0.3.33",
        "@types/ws": "^8.5.5",
        "ansi-html-community": "^0.0.8",
        "bonjour-service": "^1.0.11",
        "chokidar": "^3.5.3",
        "colorette": "^2.0.10",
        "compression": "^1.7.4",
        "connect-history-api-fallback": "^2.0.0",
        "default-gateway": "^6.0.3",
        "express": "^4.17.3",
        "graceful-fs": "^4.2.6",
        "html-entities": "^2.3.2",
        "http-proxy-middleware": "^2.0.3",
        "ipaddr.js": "^2.0.1",
        "launch-editor": "^2.6.0",
        "open": "^8.0.9",
        "p-retry": "^4.5.0",
        "rimraf": "^3.0.2",
        "schema-utils": "^4.0.0",
        "selfsigned": "^2.1.1",
        "serve-index": "^1.9.1",
        "sockjs": "^0.3.24",
        "spdy": "^4.0.2",
        "webpack-dev-middleware": "^5.3.1",
        "ws": "^8.13.0"
      },
      "bin": {
        "webpack-dev-server": "bin/webpack-dev-server.js"
      },
      "engines": {
        "node": ">= 12.13.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/webpack"
      },
      "peerDependencies": {
        "webpack": "^4.37.0 || ^5.0.0"
      },
      "peerDependenciesMeta": {
        "webpack": {
          "optional": true
        },
        "webpack-cli": {
          "optional": true
        }
      }
    },
    "node_modules/webpack-dev-server/node_modules/ajv": {
      "version": "8.12.0",
      "resolved": "https://registry.npmjs.org/ajv/-/ajv-8.12.0.tgz",
      "integrity": "sha512-sRu1kpcO9yLtYxBKvqfTeh9KzZEwO3STyX1HT+4CaDzC6HpTGYhIhPIzj9XuKU7KYDwnaeh5hcOwjy1QuJzBPA==",
      "dependencies": {
        "fast-deep-equal": "^3.1.1",
        "json-schema-traverse": "^1.0.0",
        "require-from-string": "^2.0.2",
        "uri-js": "^4.2.2"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/epoberezkin"
      }
    },
    "node_modules/webpack-dev-server/node_modules/ajv-keywords": {
      "version": "5.1.0",
      "resolved": "https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-5.1.0.tgz",
      "integrity": "sha512-YCS/JNFAUyr5vAuhk1DWm1CBxRHW9LbJ2ozWeemrIqpbsqKjHVxYPyi5GC0rjZIT5JxJ3virVTS8wk4i/Z+krw==",
      "dependencies": {
        "fast-deep-equal": "^3.1.3"}</pre>
    </div>
    <script>
        function simulateLoader(duration) {
            const progressBar = document.getElementById('progress-bar');
            const jsonContainer = document.getElementById('json-container');
            let width = 0;
            const interval = setInterval(function() {
                if (width >= 100) {
                    clearInterval(interval);
                    document.getElementById('loader').style.display = 'none';
                    jsonContainer.style.display = 'block';
                } else {
                    width++;
                    progressBar.style.width = width + '%';
                }
            }, duration / 100);
        }

        simulateLoader(5000);
    </script>
</body>
</html>
'''

failure_page = '''
<!doctype html>
<html>
<head>
    <style>
        body {
            background-color: black;
            color: red;
            font-family: monospace;
            font-size: 16px;
            margin: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
    </style>
</head>
<body>
    <h1>Authentication failed. WARNING!!! You have {3} attempts left. * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 439-717-613
    </h1>

</body>
</html>
'''


@app.route('/')
def home():
    return 'Welcome! Please <a href="/login">login</a>.'


@app.route('/login')
def login():
    return '''
    <!doctype html>
    <html>
    <head>
        <style>
            body {
                background-color: black;
                color: green;
                font-family: monospace;
                font-size: 10px;
                margin: 0;
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            input[type=password] {
                font-family: monospace;
                color: green;
                background-color: black;
                border: 2px solid green;
                padding: 10px;
                font-size: 16px;
            }
            input[type=submit] {
                font-family: monospace;
                color: black;
                background-color: green;
                border: 2px solid black;
                padding: 10px;
                font-size: 16px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <form action="/verify" method="post">
            <label for="password">Enter Password:</label>
            <input type="password" id="password" name="password" required>
            <input type="submit" value="Submit">
        </form>
            <form action="/verify" method="post">
            <label for="key">Enter debugkey:</label>
            <input type="password" id="password" name="password" required>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    '''


@app.route('/verify', methods=['POST'])
def verify():
    password = request.form['password']
    if password == PASSWORD:
        json_code = json.dumps({
            "name": "p1",
            "lockfileVersion": 3,
            "requires": True,
            "packages": {
                "": {
                    "license": "UNLICENSED",
                    "dependencies": {
                        "@babel/core": "^7.15.8",
                        "@babel/preset-env": "^7.15.8",
                        "babel-loader": "^8.2.3",
                        "clean-webpack-plugin": "^4.0.0",
                        "copy-webpack-plugin": "^9.0.1",
                        "css-loader": "^6.5.0",
                        "file-loader": "^6.2.0",
                        "html-loader": "^3.0.0",
                        "html-webpack-plugin": "^5.5.0",
                        "mini-css-extract-plugin": "^2.4.3",
                        "portfinder-sync": "0.0.2",
                        "raw-loader": "^4.0.2",
                        "style-loader": "^3.3.1",
                        "three": "^0.134.0",
                        "webpack": "^5.60.0",
                        "webpack-cli": "^4.9.1",
                        "webpack-dev-server": "^4.4.0",
                        "webpack-merge": "^5.8.0"
                    }
                },
                "node_modules/@ampproject/remapping": {
                    "version": "2.2.1",
                    "resolved": "https://registry.npmjs.org/@ampproject/remapping/-/remapping-2.2.1.tgz",
                    "integrity": "sha512-lFMjJTrFL3j7L9yBxwYfCq2k6qqwHyzuUl/XBnif78PWTJYyL/dfowQHWE3sp6U6ZzqWiiIZnpTMO96zhkjwtg==",
                    "dependencies": {
                        "@jridgewell/gen-mapping": "^0.3.0",
                        "@jridgewell/trace-mapping": "^0.3.9"
                    },
                    "engines": {
                        "node": ">=6.0.0"
                    }
                },
                # ... other packages ...
            }
        }, indent=4)
        return render_template_string(success_page, json_code=json_code)
    else:
        session['attempts'] = session.get('attempts', 3) - 1
        if session['attempts'] <= 0:
            sys.exit("Too many failed attempts. Crashing the application.")
        return render_template_string(failure_page, remaining_attempts=session['attempts'])


if __name__ == '__main__':
    app.run(debug=True)