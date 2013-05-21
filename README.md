uuidBabyName
============

A python utility to turn a 36 hex-char UUID into a human-pronounceable baby name. Inspired by Darius "@tinysubversions" Kazemi: https://twitter.com/tinysubversions/status/336947808059936769

The pronounceability gag is stolen from hastebin, http://hastebin.com/, with their clever alternate-consonants-and-vowels trick.

The name-generation itself is fully deterministic, which is an interesting twist to me: a lot of the fun CPU-generated-text stuff I do depends on a random number generator to produce its fun outcomes (a la @fakespearean, http://twitter.com/fakespearean). I guess in this case I'm just outsourcing the RNG to the UUID part. But it's still cool that these names are kind of hiding inside the ugly "55ed2e23-bb45-4e25-abff-033a42927663" string -- given the UUID, we don't need to rely on (additional) luck in order to reveal the name "Wa Meka Rutoki-Boporez-Yu."

My favorite name yet: "edf881dc-c811-4e71-b316-3b3ad48ffe71" actually means "Fito Gipupod."

A WARNING: Some steps it takes, like stripping out multiple consecutive whitespace characters, means that the baby names are no longer (necessarily) unique themselves. Two different UUIDs can yield the same baby name.

SOME EXAMPLE RESULTS
--------------------

`a017b48a-a9d5-4cf0-b581-17497cec392c` =>  **Goq Tem Gosoy Pilu**

`baa8816b-39a1-41c1-a2f9-7c4a106aa6f7` =>  **Pi Ra Sufec**

`b3e00c6a-58d7-41c6-9781-952b1950d013` =>  **Dic-wo Ram Lohavay Fu**

`d93bbd75-d2d6-4198-b281-47aa4ecd3339` =>  **Pu Rah Sed To Nepi**

`14bb5472-5e3f-46da-904f-c7239d3f70a2` =>  **Ga Vum Xuqosal Tu Ka Qok**

`5a8ac2ba-0e2b-45a1-88fa-081eff24555d` =>  **Xaq Duloru Coja Kewaxo**

`19c21ba7-3538-42b3-9eef-b16a0aa9604e` =>  **Hah Hi Nopere Da Yeto**

`4a0c12c7-a0ec-4a87-94cf-c19574188e3d` =>  **Sudifo Su Guv Qe**

`b6d489eb-541c-44e5-be30-ea872fe0e55c` =>  **Vuhoro Mof Mis Xi**

`366d0883-929d-4a61-aa1d-06307b7259e4` =>  **Nu Co Suyid Hucemo Wux**

`37e3ac1a-4b5e-4830-a3d4-ca9b2e1feec0` =>  **Pa Hetaxusimo Mejek**

`7298bbc2-ef43-47df-a88b-458bc8c2fc0f` =>  **Rise Ru Fa**

`b4b58d97-2215-495a-aba3-9aeb2a5ee00e` =>  **Jugesoxa Lixus Du**

`42fb576c-a210-4e1a-9470-1dc7500100cb` =>  **Re Wif Fetohec Hu Vabeba**

`3e2c1183-3092-4059-a1fa-53d852260769` =>  **Qilufi Moz-quwu Voj-vikoci**

`33625c7c-5a19-47b9-bdfd-a5f601c9f79e` =>  **Neyoxiy Xahase Be**

`c99687d1-f051-4872-a8c6-a8536860122f` =>  **Vesim Vozuyefomi**

`cc3e44d9-1ec6-49b4-8c90-517d4306415a` =>  **Qiro Jam Soq Ve Riceraxa**

`b7b2b3b4-4f78-46f8-8b7b-c32a4f7a38f5` =>  **Tut Saw Lituw Pe**

`2def608c-d5bb-4df3-93bc-69e0df894011` =>  **Ma Yes Ti Qufi**

`fdfe49f3-f57d-4698-a5ca-a2f246c0749e` =>  **So Sah Saf**

`2e7c598e-5e94-48f0-a0ab-4e2368241d1b` =>  **Mey Wuv Xuc Sim Tokazukehuhi**

`7be47257-fb50-49eb-95ce-be6ecc30f77f` =>  **Wi Vaso Mo**

`6b81268e-7d07-4fde-8195-de3c9a00f10c` =>  **Kov Cituq Qak Ba Di**

`0daa5c10-899d-4b83-b43b-a47afccad78c` =>  **Dod Xife Ta Puw**

`2aad5517-f5b3-4388-b403-6fab64da86f6` =>  **Li Wago Rin-Bo Zal**

`ccbfa308-2664-4f27-a40e-09e8975954cc` =>  **Cokozatukuw Ducuc Wuvut**

`b3589546-80d9-4d42-8b69-2940a6f87c97` =>  **Wo Sad Tire Lequy**

`5dc12870-fd54-47ec-820d-ea7800131e37` =>  **Xo Lak Vuseh-Dof Bafujapa**

`9a6a4d8b-534e-466d-afae-9dabe8ffb01c` =>  **Ti Votosa Ho**

`b55461e9-2dc1-4c20-af5d-770a0fcf7f41` =>  **Vuyi Ma Teji Xo Dafa Ra**

`66e96439-b947-43c4-bf29-329e8b6e5b57` =>  **Zi Zapi Serik-Lenap Xewi**

`fd1ee402-7d62-4a0e-be24-c78689b92b60` =>  **Jax Bi Yosuduc Ke Loye**

`12336891-e5d3-46e8-a0b9-d4c0405c2e7a` =>  **Fonezu Sac Quximew**

`54ec94b8-60a9-46db-8099-ea958fc9245a` =>  **Vuh-Ye Sa Kexa**