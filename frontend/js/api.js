/*
=========================================
api.js
AI Resume Builder
=========================================
*/

"use strict";

/*
=========================================
Backend URL

For Local Development
=========================================
*/

const API_BASE_URL = "http://127.0.0.1:8000";

/*
For Render Deployment

Example

const API_BASE_URL =
"https://your-backend-name.onrender.com";

*/


/*
=========================================
Create Resume
=========================================
*/

async function createResume(resumeData) {

    showLoading();

    try {

        const response = await fetch(

            `${API_BASE_URL}/resumes/create`,

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify(resumeData)

            }

        );


        /*
        -----------------------------------------
        Backend Error
        -----------------------------------------
        */

        if (!response.ok) {

            let errorMessage = "Something went wrong.";

            try {

                const error = await response.json();

                if (error.message) {

                    errorMessage = error.message;

                }

            }

            catch {

                errorMessage =
                    "Unable to communicate with server.";

            }

            throw new Error(errorMessage);

        }


        /*
        -----------------------------------------
        Receive PDF
        -----------------------------------------
        */

        const pdfBlob = await response.blob();

        const downloadURL =
            window.URL.createObjectURL(pdfBlob);


        const link =
            document.createElement("a");


        link.href = downloadURL;

        link.download = "resume.pdf";


        document.body.appendChild(link);

        link.click();

        link.remove();

        window.URL.revokeObjectURL(downloadURL);


        showToast(

            "Resume generated successfully.",

            true

        );

    }

    catch (error) {

        console.error(error);

        /*
        Future Ready

        If backend returns

        You have reached your limit of
        3 resume downloads.

        It will automatically display here.
        */

        showToast(error.message);

    }

    finally {

        hideLoading();

    }

}