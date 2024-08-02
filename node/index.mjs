import { pipeline } from 'node:stream/promises'
import { createWriteStream } from 'node:fs'

const res = await fetch('http://0.0.0.0:5001', {
    method: 'POST',
    headers: {
        'Content-type': 'application/json'
    },
    body: JSON.stringify({
        filename: 'pack.zip'
    })
})

if (res.ok) {

    try {
        await pipeline(
            res.body,
            createWriteStream('./node/downloads/file.zip')
        )
    } catch (error) {
        console.log(error)
    }


} else {
    console.log('error')
}