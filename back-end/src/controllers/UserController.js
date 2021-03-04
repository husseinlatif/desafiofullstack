const User = require('../models/User')
const sequelize = require('../config/sequelize')


const index = async(req, res) => {
    try {
        const users = User.findAll();
        return res.status(200).json({users});
    } catch (err) {
        return res.status(500).json({err});
    }
};


const show = async(req, res) => { 
    try {
        const {id} = req.params;
        const user = await User.findByPk(id);
        return res.status(200).json({user});
    } catch (err) {
        return res.status(500).json({err});
    }
};


const create = async(req, res) => {
    const userData = {
        username: req.body.username,
        email: req.body.email,
    // inclusionDate: Date.now(),
    // alterationDate: null,
        rules: req.body.rules,
        status: req.body.status,
    };

    try {
        const newUser = await User.create(userData);
        return res.status(200).json({newUser});
    } catch (err) {
        return res.status(500).json({err});
    }
};


const update = async(req, res) => {
    const userData = {
        username: req.body.username,
        email: req.body.email,
    // alterationDate: Date.now(),
        rules: req.body.rules,
        status: req.body.status,
    };
    
    try {
        const {id} = req.params;
        const user = await User.update(userData, {where: {id: id}} )
    } catch (err) {
        return res.status(500).json({err});
    }
};


const destroy = async(req, res) => {
    try {
        const {id} = req.params;
        const deletedUser = await User.destroy(req.body, {where: {id: id}});
        if (deletedUser) {
            return res.status(200).json("Usuário deletado com sucesso!");
        }
        throw new Error("Usuário não encontrado!");
    } catch (err) {
        return res.status(500).json({err});
    }
};


module.exports = {
    index,
    show,
    create,
    update,
    destroy,
}